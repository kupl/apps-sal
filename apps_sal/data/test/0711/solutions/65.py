from collections import defaultdict


def factorize(n):
    facts = defaultdict(int)
    while n % 2 == 0:
        n //= 2
        facts[2] += 1
    m = 3
    while m * m <= n:
        while n % m == 0:
            facts[m] += 1
            n //= m
        m += 2
    if 1 < n:
        facts[n] += 1
    return facts


MOD = 10 ** 9 + 7
MAX = 10 ** 5 + 100
FACTS = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    FACTS[i] = FACTS[i - 1] * i % MOD
FACTINVS = [1] * (MAX + 1)
INVS = [1] * (MAX + 1)
for i in range(2, MAX + 1):
    (q, r) = divmod(MOD, i)
    INVS[i] = -INVS[r] * q % MOD
    FACTINVS[i] = FACTINVS[i - 1] * INVS[i] % MOD


def nCr(n, r):
    return FACTS[n] * FACTINVS[r] * FACTINVS[n - r]


(N, M) = map(int, input().split())
factors = factorize(M)
ans = 1
for (p, e) in factors.items():
    ans = ans * nCr(N - 1 + e, e) % MOD
print(ans)
