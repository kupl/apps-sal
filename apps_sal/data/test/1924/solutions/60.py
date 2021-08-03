MOD = 10 ** 9 + 7
FACT_MAX = 2 * 10 ** 6 + 3
fact = [1] * FACT_MAX
for i in range(1, FACT_MAX):
    fact[i] = fact[i - 1] * i % MOD


def comb(n, r):
    return fact[n] * pow(fact[n - r], MOD - 2, MOD) * pow(fact[r], MOD - 2, MOD)


def g(r, c):
    return (comb(r + c + 2, c + 1) - 1) % MOD


r1, c1, r2, c2 = list(map(int, input().split()))
print(((g(r2, c2) - g(r2, c1 - 1) - g(r1 - 1, c2) + g(r1 - 1, c1 - 1)) % MOD))
