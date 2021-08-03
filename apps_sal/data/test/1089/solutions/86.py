def comb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)
############################################################

N, M, K = map(int, input().split())
MOD = 10**9 + 7
sumx = 0
sumy = 0

for d in range(1, N):
    cnt = (N - d) * M**2
    cnt %= MOD
    cnt *= comb(N * M - 2, K - 2, MOD)
    sumx += d * cnt
    sumx %= MOD

for d in range(1, M):
    cnt = (M - d) * N**2
    cnt %= MOD
    cnt *= comb(N * M - 2, K - 2, MOD)
    sumy += d * cnt
    sumy %= MOD
print((sumx + sumy) % MOD)
