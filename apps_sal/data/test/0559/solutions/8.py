import numpy as np
mod = 998244353


def poly_mul(f, g):
    Lf = len(f)
    Lg = len(g)
    L = Lf + Lg - 1
    if Lf <= 16 or Lg <= 16:
        if Lf == 0 or Lg == 0:
            return np.zeros((0,), dtype=np.int64)
        return (np.convolve(f.astype(np.uint64), g.astype(np.uint64)) % mod).astype(np.int64)
    fft = np.fft.rfft
    ifft = np.fft.irfft
    fft_len = 1 << L.bit_length()
    fl = f & (1 << 15) - 1
    fh = f >> 15
    gl = g & (1 << 15) - 1
    gh = g >> 15
    x = (ifft(fft(fl, fft_len) * fft(gl, fft_len))[:L] + 0.5).astype(np.int64) % mod
    y = (ifft(fft(fl + fh, fft_len) * fft(gl + gh, fft_len))[:L] + 0.5).astype(np.int64) % mod
    z = (ifft(fft(fh, fft_len) * fft(gh, fft_len))[:L] + 0.5).astype(np.int64) % mod
    return (x + ((y - x - z) << 15) + (z << 30)) % mod


def poly_inv(fps, n=None):
    assert fps[0] != 0
    if n is None:
        n = len(fps)
    res = np.zeros(1 << (n - 1).bit_length(), dtype=np.int64)
    res[0] = pow(int(fps[0]), mod - 2, mod)
    i = 1
    while i < n:
        i <<= 1
        res[:i] = ((res[:i] << 1) - poly_mul(poly_mul(res[:i >> 1], res[:i >> 1]), fps[:i])[:i]) % mod
    return res[:n]


def poly_div(fps1, fps2):
    n1, n2 = len(fps1), len(fps2)
    if n1 < n2:
        return np.zeros((0,), dtype=np.int64)
    n = n1 - n2 + 1
    res = poly_mul(fps1[-1:-n - 1:-1], poly_inv(fps2[::-1], n))[n - 1::-1]
    return res


def poly_mod(fps1, fps2):
    n1, n2 = len(fps1), len(fps2)
    if n1 < n2:
        return fps1
    res = fps1[:n2 - 1] - poly_mul(poly_div(fps1, fps2), fps2)[:n2 - 1]
    return res % mod


def multipoint_evaluation(fps, xs):
    threshold = 8
    n_xs = len(xs)
    bit = (n_xs - 1).bit_length()
    if bit <= threshold:
        res = np.zeros_like(xs)
        xs_cumprod = np.ones_like(xs)
        for coef in fps:
            res += xs_cumprod * coef
            xs_cumprod *= xs
            xs_cumprod %= mod
        return res
    k = 1 << bit
    fpss = np.zeros((bit + 1, k + 1), dtype=fps.dtype)
    fpss[0, :n_xs] = -xs % mod
    fpss[1, :k:2] = fpss[0, :k:2] * fpss[0, 1::2] % mod
    fpss[1, 1::2] = (fpss[0, :k:2] + fpss[0, 1::2]) % mod
    for i in range(1, bit):
        step = 2 << i
        half = step >> 1
        for j in range(0, k, step):
            f1 = fpss[i, j:j + half + 1].copy()
            f2 = fpss[i, j + half:j + step + 1].copy()
            f1[-1] = f2[-1] = 1
            f = poly_mul(f1, f2)
            fpss[i + 1, j:j + step] = f[:-1]
    f = poly_mod(fps, f)
    fpss[-1, :len(f)] = f
    fpss[-1, len(f):] = 0
    for i in range(bit - 1, threshold - 1, -1):
        step = 2 << i
        half = step >> 1
        for j in range(0, k, step):
            f = fpss[i + 1, j:j + step]
            f1 = fpss[i, j:j + half + 1].copy()
            f2 = fpss[i, j + half:j + step + 1].copy()
            f1[-1] = f2[-1] = 1
            fpss[i, j:j + half] = poly_mod(f, f1)
            fpss[i, j + half:j + step] = poly_mod(f, f2)
    xs = (-fpss[0, :k] % mod).reshape(-1, 1 << threshold)
    xs_cumprod = np.ones_like(xs)
    res = np.zeros_like(xs)
    for i in range(1 << threshold):
        res += fpss[threshold, i:k:1 << threshold, None] * xs_cumprod % mod
        xs_cumprod *= xs
        xs_cumprod %= mod
    return res.reshape(-1)[:n_xs] % mod


def poly_differential(fps):
    return fps[1:] * np.arange(1, len(fps)) % mod


def lagrange_interpolation(X, Y, mod):
    n = len(X)
    g = [0] * (n + 1)
    g[0] = 1
    for i, x in enumerate(X):
        for j in range(i, -1, -1):
            g[j + 1] += g[j] * (-x) % mod
    res = [0] * n
    for x, y in zip(X, Y):
        f = g[:]
        denom = 0
        v = 1
        pow_x = [1]
        for _ in range(n - 1):
            v = v * x % mod
            pow_x.append(v)
        pow_x.reverse()
        for i, po in enumerate(pow_x):
            f_i = f[i]
            f[i + 1] += f_i * x % mod
            denom = (denom + f_i * po) % mod
        denom_inv = pow(denom, mod - 2, mod)
        for i, f_i in enumerate(f[:n]):
            res[i] += (f_i * y * denom_inv)
    return [v % mod for v in res]


def polynomial_interpolation(xs, ys):
    assert len(xs) == len(ys)
    threshold = 8
    as_strided = np.lib.stride_tricks.as_strided
    n = len(xs)
    if n == 1:
        return ys.copy()
    bit = (n - 1).bit_length()
    if bit <= threshold:
        res = lagrange_interpolation(xs.tolist(), ys.tolist(), mod)
        return np.array(res[::-1], dtype=np.int64)
    k = 1 << bit
    fpss = np.zeros((bit + 1, n + 1), dtype=np.int64)
    fpss[0, :n] = -xs % mod
    for i in range(bit):
        step = 2 << i
        half = step >> 1
        for j in range(0, n, step):
            if j + half >= n:
                fpss[i + 1, j:n] = fpss[i, j:n]
                continue
            f1 = fpss[i, j:j + half + 1].copy()
            f2 = fpss[i, j + half:j + step + 1].copy()
            f1[-1] = f2[-1] = 1
            f = poly_mul(f1, f2)
            fpss[i + 1, j:j + len(f) - 1] = f[:-1]
    fpss2 = np.zeros((bit + 1, k + 1), dtype=np.int64)
    fpss2[bit, :n] = poly_differential(f)
    for i in range(bit - 1, threshold - 1, -1):
        step = 2 << i
        half = step >> 1
        for j in range(0, n, step):
            if j + half >= n:
                fpss2[i, j:n] = fpss2[i + 1, j:n]
                continue
            f = fpss2[i + 1, j:min(j + step, n)]
            f1 = fpss[i, j:j + half + 1].copy()
            f2 = fpss[i, j + half:min(j + step, n) + 1].copy()
            f1[-1] = f2[-1] = 1
            fpss2[i, j:j + half] = poly_mod(f, f1)
            fpss2[i, j + half:min(j + step, n)] = poly_mod(f, f2)
    xs = as_strided(xs, (k >> threshold, 1 << threshold), (8 << threshold, 8))
    xs_cumprod = np.ones_like(xs)
    f = np.zeros_like(xs)
    for i in range(1 << threshold):
        f += fpss2[threshold, i:k:1 << threshold, None] * xs_cumprod % mod
        xs_cumprod *= xs
        xs_cumprod %= mod
    f = f.ravel()
    for j in range(n):
        fpss2[0, j] = ys[j] * pow(int(f[j]), mod - 2, mod) % mod
    for i in range(bit):
        step = 2 << i
        half = step >> 1
        for j in range(0, k, step):
            if j + half >= n:
                fpss2[i + 1, j:n] = fpss2[i, j:n]
                continue
            f1 = fpss[i, j:j + half + 1].copy()
            f2 = fpss[i, j + half:j + step + 1].copy()
            f1[-1] = f2[-1] = 1
            fpss2[i + 1, j:min(j + step, n)] = (
                poly_mul(fpss2[i, j:j + half], f2)
                + poly_mul(fpss2[i, j + half:min(j + step, n)], f1)
            ) % mod
    return fpss2[bit, :n]


mod = int(input())
A = np.array(input().split(), dtype=np.int64)
X = np.arange(mod, dtype=np.int64)
Ans = polynomial_interpolation(X, A)
print((" ".join(map(str, Ans.tolist()))))
