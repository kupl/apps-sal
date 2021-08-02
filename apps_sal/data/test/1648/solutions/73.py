n, k = map(int, input().split())
mod = 10**9 + 7


def nCr(N, R, mod):
    R = min(R, N - R)
    numer = denom = 1
    for i in range(1, R + 1):
        numer = numer * (N + 1 - i) % mod
        denom = denom * i % mod
    res = numer * pow(denom, mod - 2, mod) % mod
    return res


for i in range(1, k + 1):
    if n - k + 1 < i:
        print(0)
        continue
    y = nCr(n - k + 1, i, mod)
    y *= nCr(k - 1, i - 1, mod)
    print(y % mod)
