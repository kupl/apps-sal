N, M, K = map(int, input().split())
MOD = 10**9 + 7

MAXN = N * M + 5
fac = [1, 1] + [0] * MAXN
finv = [1, 1] + [0] * MAXN
inv = [0, 1] + [0] * MAXN
for i in range(2, MAXN + 2):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = -inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, r):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD


a = 0
for d in range(1, N):
    a += d * (N - d) * M * M
b = 0
for d in range(1, M):
    b += d * (M - d) * N * N
ans = (a + b) * comb(N * M - 2, K - 2)
ans %= MOD
print(ans)
