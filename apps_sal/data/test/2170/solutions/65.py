import math
MOD = 10 ** 9 + 7

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

def init(n):
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        factinv.append((factinv[-1] * inv[-1]) % MOD)

def nPk(n, k):
    return fact[n] * factinv[n - k] % MOD

def nCk(n, k):
    return fact[n] * factinv[n - k] * factinv[k] % MOD

N, M = list(map(int, input().split()))
init(M)
ans = 0
for k in range(N + 1):
    if k % 2 == 0:
        ans += nCk(N, k) * nPk(M - k, N - k)
    else:
        ans -= nCk(N, k) * nPk(M - k, N - k)
    ans = (ans + MOD) % MOD
ans *= nPk(M, N)
ans %= MOD
print(ans)

