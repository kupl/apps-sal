MOD = 10 ** 9 + 7
table_len = 500010

fac = [1, 1]
for i in range(2, table_len):
    fac.append(fac[-1] * i % MOD)

finv = [0] * table_len
finv[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(table_len - 1, -1, -1):
    finv[i - 1] = finv[i] * i % MOD


def comb(n, k):
    return fac[n] * finv[k] * finv[n - k] % MOD


def perm(n, k):
    return fac[n] * finv[n - k] % MOD


N, M = list(map(int, input().split()))

print((sum(((-1)**k * comb(N, k) * perm(M, k) * perm(M - k, N - k)**2 % MOD) for k in range(N + 1)) % MOD))
