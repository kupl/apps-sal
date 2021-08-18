N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

MOD = 10 ** 9 + 7

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]


def cmb(n, k, p):
    if (k < 0) or (n < k):
        return 0
    r = min(k, n - k)
    return fact[n] * factinv[k] * factinv[n - k] % p


for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

A.sort()

ans = 0
for i in range(N - K + 1):
    ans += A[-1 - i] * cmb(N - i - 1, K - 1, MOD)
    ans -= A[i] * cmb(N - i - 1, K - 1, MOD)
    ans %= MOD

print((ans % MOD))
