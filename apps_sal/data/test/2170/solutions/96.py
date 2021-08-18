
N, M = map(int, input().split())
MOD = 10 ** 9 + 7

fac = [1, 1]
inv = [0, 1]
finv = [1, 1]

for i in range(2, M + 1):
    fac.append(fac[-1] * i % MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    finv.append(finv[-1] * inv[-1] % MOD)

fixed = (fac[N] * fac[M] * pow(finv[M - N], 2, MOD)) % MOD


def f(k):
    return (fac[M - k] * finv[k] * finv[N - k]) % MOD


ans = 0
for i in range(N + 1):
    ans = (ans + fixed * f(i) * pow(-1, i)) % MOD

print(ans)
