MOD = 10 ** 9 + 7
(r1, c1, r2, c2) = list(map(int, input().split()))


def getComb(n, k, MOD):
    if n < k:
        return 0
    if n - k < k:
        k = n - k
    comb = 1
    for x in range(n - k + 1, n + 1):
        comb = comb * x % MOD
    d = 1
    for x in range(1, k + 1):
        d = d * x % MOD
    comb *= pow(d, MOD - 2, MOD)
    return comb % MOD


def f(i, j):
    return getComb(i + j, j, MOD)


ans = f(r2 + 1, c2 + 1) - f(r2 + 1, c1) - f(r1, c2 + 1) + f(r1, c1)
ans %= MOD
print(ans)
