N, M = map(int, input().split())
MOD = 10**9 + 7

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


ans = 1
for i in range(N):
    ans *= (M - i)
    ans %= MOD

ps = [1]
for i in range(N):
    ps.append((ps[-1] * (M - N + 1 + i)) % MOD)
ps.reverse()

tmp = 0
for i, p in enumerate(ps):
    t = p * comb(N, i)
    if i % 2:
        t *= -1
    tmp += t

ans *= tmp
ans %= MOD
print(ans)
