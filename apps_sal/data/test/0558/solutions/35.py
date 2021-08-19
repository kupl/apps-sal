import math
n, m, k = map(int, input().split())


def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


MOD = 998244353
N = 3 * 10 ** 5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod MOD)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod MOD)
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

ans = 0
for kk in range(k + 1):
    ans_kk = m * cmb(n - 1, kk, MOD) * pow(m - 1, n - kk - 1, MOD)
    ans = (ans + ans_kk) % MOD

print(ans)
