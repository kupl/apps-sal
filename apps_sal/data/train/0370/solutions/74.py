class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.s = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:
    sieve = [0] * 100001
    for i in range(2, 100001):
        if sieve[i] != 0:
            continue
        for j in range(1, 100000 // i + 1):
            sieve[j * i] = i

    def largestComponentSize(self, A: List[int]) -> int:
        def add_prime(q, i, primes):
            if q not in primes:
                primes[q] = [i]
            else:
                primes[q].append(i)
        n = len(A)
        g = UF(n)
        primes = {}
        for i, k in enumerate(A):
            while k > 1:
                q = self.sieve[k]
                add_prime(q, i, primes)
                while k % q == 0:
                    k //= q
        # print(primes)
        for l in primes.values():
            j, r = l[0], g.find(l[0])
            for i in l[1:]:
                nd = g.find(i)
                if nd != r:
                    g.p[nd] = r
                    g.s[r] += g.s[nd]
        # print(g.p)
        # print(g.s)
        return max(g.s)
