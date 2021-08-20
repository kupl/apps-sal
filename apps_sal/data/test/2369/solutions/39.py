(N, K) = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
MOD = 10 ** 9 + 7
MAXN = N + 5
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


ans = 0
for n in range(K - 1, N):
    c = comb(n, K - 1)
    mx = A[n]
    mn = A[-1 - n]
    ans += (mx - mn) * c
    ans %= MOD
print(ans)
