L, R = map(int, input().split())

mod = 10**9 + 7
m = 64 + 1
fac = [1] * m
ninv = [1] * m
finv = [1] * m
for i in range(2, m):
    fac[i] = fac[i - 1] * i % mod
    ninv[i] = (-(mod // i) * ninv[mod % i]) % mod
    finv[i] = finv[i - 1] * ninv[i] % mod


def comb(n, k):
    return (fac[n] * finv[k] % mod) * finv[n - k] % mod


def f(L, R):
    if L > R:
        return 0
    R = bin(R)[2:]
    N = len(R)
    ret = f(L, int("0" + "1" * (N - 1), 2))
    L = bin(L)[2:]
    if len(L) != N:
        L = "1" + "0" * (N - 1)
    for i in range(N):
        if R[i] == "0":
            continue
        R2 = R[:i] + "0" + "?" * (N - i - 1)
        if i == 0:
            R2 = R
        for j in range(N):
            if L[j] == "1" and j != 0:
                continue
            L2 = L[:j] + "1" + "?" * (N - j - 1)
            if j == 0:
                L2 = L
            if L2[0] == "0":
                break
            tmp = 1
            for r, l in zip(R2[1:], L2[1:]):
                if r == "0" and l == "1":
                    tmp *= 0
                if r == "?" and l == "?":
                    tmp *= 3
                if r == "?" and l == "0":
                    tmp *= 2
                if r == "1" and l == "?":
                    tmp *= 2
                tmp %= mod
            ret += tmp
            ret %= mod
    return ret % mod


print(f(L, R))
