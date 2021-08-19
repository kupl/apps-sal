(N, M, K) = list(map(int, input().split()))
MOD = 10 ** 9 + 7
MAXN = N * M + 10
fac = [1, 1] + [0] * MAXN
finv = [1, 1] + [0] * MAXN
inv = [0, 1] + [0] * MAXN
for i in range(2, MAXN + 2):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = -inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def nCr(n, r):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD


ans = 0
for i in range(1, M + 1):
    tmp = i * N % MOD * (2 * i - 1 - M) % MOD * N % MOD
    tmp *= nCr(N * M - 2, K - 2)
    tmp %= MOD
    ans += tmp
    ans %= MOD
for i in range(1, N + 1):
    tmp = i * M % MOD * (2 * i - 1 - N) % MOD * M % MOD
    tmp *= nCr(N * M - 2, K - 2)
    tmp %= MOD
    ans += tmp
    ans %= MOD
print(ans)
