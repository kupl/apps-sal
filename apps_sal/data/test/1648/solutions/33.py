def comb(n, r, p):
    if n < r:
        return 0
    elif n < 0 or r < 0:
        return 0
    return fac[n] * (facinv[r] * facinv[n - r] % p) % p


def comb_pre(N, p):
    for i in range(2, N + 1):
        fac.append(fac[i - 1] * i % p)
        inv.append(-inv[p % i] * (p // i) % p)
        facinv.append(facinv[-1] * inv[-1] % p)


fac = [1, 1]
facinv = [1, 1]
inv = [0, 1]
(N, K) = list(map(int, input().split()))
MOD = 1000000007
comb_pre(N, MOD)
for i in range(1, K + 1):
    tmp = comb(N - K + 1, i, MOD)
    tmp %= MOD
    tmp *= comb(K - 1, i - 1, MOD)
    tmp %= MOD
    print(tmp)
