# D - Factorization

N, M = map(int, input().split())
MOD = 10**9 + 7


def prime_factorization(n):
    prime_factors = []
    if n < 2:
        return 0
    for i in range(2, int(pow(n, 0.5) + 1)):
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            prime_factors.append((i, ex))
    if n != 1:
        prime_factors.append((n, 1))
    return prime_factors


fac = [1, 1]
inv = [0, 1]
finv = [1, 1]

for i in range(2, N + 36):
    fac.append(fac[-1] * i % MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    finv.append(finv[-1] * inv[-1] % MOD)


def comb_mod(n, r, m):
    if (n < 0 or r < 0 or n < r): return 0
    r = min(r, n - r)
    return fac[n] * finv[n - r] * finv[r] % m


primes = prime_factorization(M)
ans = 1
if primes != 0:
    for (p, ex) in primes:
        ans = (ans * comb_mod(ex + N - 1, N - 1, MOD)) % MOD

print(ans)
