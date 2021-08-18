n, m, k = list(map(int, input().split()))

MOD = 998244353
fact = [1] * (n + 1)
factinv = [1] * (n + 1)
for i in range(n):
    fact[i + 1] = fact[i] * (i + 1) % MOD
    factinv[i + 1] = pow(fact[i + 1], MOD - 2, MOD)


def nCk(n, k):
    return fact[n] * factinv[n - k] * factinv[k] % MOD


ans = 0
for i in range(k + 1):
    ans += m * pow(m - 1, n - 1 - i, MOD) * nCk(n - 1, i) % MOD

print((ans % MOD))
