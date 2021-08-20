MOD = 998244353
fac = [1] * (10 ** 6 + 10)
for i in range(len(fac) - 1):
    fac[i + 1] = fac[i] * (i + 1) % MOD


def nCr(n, r):
    if n < 0 or r < 0 or n < r:
        return 0
    return fac[n] * pow(fac[n - r], MOD - 2, MOD) * pow(fac[r], MOD - 2, MOD) % MOD


(n, k) = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += nCr(n // (i + 1) - 1, k - 1)
print(ans % MOD)
