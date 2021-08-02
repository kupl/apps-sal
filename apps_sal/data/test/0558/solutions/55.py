N, M, K = list(map(int, input().split()))
MOD = 998244353
if M == 1:
    print((1 if K == N - 1 else 0))
    return

MAXN = N + 5
fac = [1, 1] + [0] * MAXN
finv = [1, 1] + [0] * MAXN
inv = [0, 1] + [0] * MAXN
for i in range(2, MAXN + 2):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = -inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD


cs = []
ms = [(M * pow(M - 1, N - 1 - K, MOD)) % MOD]
for i in range(K + 1):
    cs.append(comb(N - 1, i))
    if i:
        ms.append((ms[-1] * (M - 1)) % MOD)

ans = 0
for c, m in zip(cs, ms[::-1]):
    ans += c * m
print((ans % MOD))
