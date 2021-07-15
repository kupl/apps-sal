N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A.sort()

MOD = 10 ** 9 + 7

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]


def cmb(n, k, p):
    nonlocal fact, factinv
    if (k < 0) or (n < k):
        return 0
    r = min(k, n - k)
    return fact[n] * factinv[k] * factinv[n - k] % p


for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)


masum = 0
misum = 0
ans = 0

for i in range(N - (K - 1)):
    x = cmb(N - i - 1, K - 1, MOD)
    ans += A[-i - 1] * x
    ans -= A[i] * x
    ans %= MOD

print(ans)




