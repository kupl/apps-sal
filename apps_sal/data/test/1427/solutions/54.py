import numpy as np


class SieveOfEratosthenes:
    def __init__(self, V):
        self.is_prime = np.ones(V + 1, dtype=bool)
        self.is_prime[4::2] = False
        self.is_prime[9::3] = False
        self.is_prime[25::5] = False
        self.primes = [2, 3, 5]
        for i in range(7, V + 1, 2):
            if self.is_prime[i]:
                self.primes.append(i)
                self.is_prime[i * i::i] = False

    def factorize(self, x):
        assert x >= 1
        if x == 1:
            return [(1, 1)]
        result = []
        for p in self.primes:
            exp = 0
            while x % p == 0:
                exp += 1
                x = x // p
            if exp > 0:
                result.append((p, exp))
            if p * p > x:
                break
        if x > 1:
            result.append((x, 1))
        return result


N = int(input())
M = 10**9 + 7
A = list(map(int, input().split()))

sieve = SieveOfEratosthenes(10**3)
F = [dict(sieve.factorize(a)) for a in A]

lcm = F[0]
for i in range(1, len(F)):
    for p, e in list(F[i].items()):
        if p in lcm:
            lcm[p] = max(lcm[p], e)
        else:
            lcm[p] = e

val = 1
for p, e in list(lcm.items()):
    val = val * pow(p, e, M) % M
# print(val)

B = [val * pow(a, M - 2, M) % M for a in A]
print((sum(B) % M))
