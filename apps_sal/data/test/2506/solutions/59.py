import sys
import numpy as np

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def convolve(f, g):
    """多項式 f, g の積を計算する。

    Parameters
    ----------
    f : np.ndarray (int64)
        f[i] に、x^i の係数が入っている

    g : np.ndarray (int64)
        g[i] に、x^i の係数が入っている


    Returns
    -------
    h : np.ndarray
        f,g の積
    """
    fft_len = 1
    while 2 * fft_len < len(f) + len(g) - 1:
        fft_len *= 2
    fft_len *= 2

    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)

    Fh = Ff * Fg

    h = np.fft.irfft(Fh, fft_len)

    h = np.rint(h).astype(np.int64)

    return h


N, M = inl()
A = inl()

power = np.zeros(10 ** 5 + 1, dtype=np.int64)
for i in range(N):
    power[A[i]] += 1

P = convolve(power, power)

r = M
ans = 0
for k in range(len(P) - 1, -1, -1):
    c = min(P[k], r)
    ans += k * c
    r -= c
    if r <= 0:
        break

print(ans)
