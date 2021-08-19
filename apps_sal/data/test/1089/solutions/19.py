def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a % 1000000007
    elif b % 2 == 0:
        return power(a, b // 2) ** 2 % 1000000007
    else:
        return power(a, b // 2) ** 2 * a % 1000000007


def divide(a, b):
    return a * power(b, 1000000005) % 1000000007


fac_lim = 200000
fac = [None] * (fac_lim + 1)
fac[0] = 1
for i in range(fac_lim):
    fac[i + 1] = fac[i] * (i + 1)
    fac[i + 1] = fac[i + 1] % 1000000007
fac_inv = [None] * (fac_lim + 1)
fac_inv[fac_lim] = power(fac[fac_lim], 1000000005)
for i in range(fac_lim, 0, -1):
    fac_inv[i - 1] = fac_inv[i] * i % 1000000007


def conv(a, b):
    return fac[a] * fac_inv[a - b] * fac_inv[b] % 1000000007


MOD = 1000000007
(N, M, K) = (int(i) for i in input().split())
midN = 0
midM = 0
if N > 1:
    for i in range(1, N):
        midN += i * (N - i) * 2
        midN % MOD
    midN = divide(midN, N ** 2)
else:
    midN = 0
if M > 1:
    for i in range(1, M):
        midM += i * (M - i) * 2
        midM % MOD
    midM = divide(midM, M ** 2)
else:
    midM = 0
kt = (midN + midM) * (N * M)
kt = divide(kt, N * M - 1)
pt = conv(N * M, K)
ans = kt * pt % MOD
ans = ans * K * (K - 1) % MOD
ans = divide(ans, 2)
print(ans % MOD)
