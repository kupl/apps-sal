def solve(L, A, B, M):
    ret, digits = 0, 0
    for d in range(18, 0, -1):
        lo = 10 ** (d - 1)
        hi = 10 ** d - 1
        if hi < A or A + B * (L - 1) < lo:
            continue
        imin = 0 if lo <= A else (lo - A + B - 1) // B
        init = A + B * imin
        if init > hi:
            continue
        imax = L - 1 if A + B * (L - 1) <= hi else imin + (hi - init) // B
        n = imax - imin + 1
        p = 10 ** d % M
        a = matpow([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, p, p], [0, 0, 0, p]], n, M)
        # a[0][3] = sum p^i for i in [0, n-1]
        # a[1][3] = sum i * p^i for i in [0, n-1]
        # sum (A + B * (imax - i)) * p^i for i in [0, n-1]
        sub = (A + B * imax) % M * a[1][3] % M + M - (B * a[0][3] % M)
        ret += sub % M * pow10(digits, M) % M
        digits += d * (imax - imin + 1)
    return ret % M


def pow10(p, mod):
    if p % 2 == 1:
        return 10 * pow10(p - 1, mod) % mod
    elif p > 0:
        sub = pow10(p // 2, mod)
        return sub * sub % mod
    else:
        return 1


def matpow(a, p, mod):
    if p % 2 == 1:
        return matmul(a, matpow(a, p - 1, mod), mod)
    elif p > 0:
        b = matpow(a, p // 2, mod)
        return matmul(b, b, mod)
    else:
        n = len(a)
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matmul(a, b, mod):
    n = len(a)
    ret = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                ret[i][j] += a[i][k] * b[k][j]
        for j in range(n):
            ret[i][j] %= mod
    return ret


L, A, B, M = list(map(int, input().split()))
print((solve(L, A, B, M)))

