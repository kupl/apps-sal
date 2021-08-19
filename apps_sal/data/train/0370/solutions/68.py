class DSU:

    def __init__(self, n):
        self.sets = list(range(n))
        self.sizes = [1] * n

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.sizes[x] < self.sizes[y]:
                (x, y) = (y, x)
            self.sets[y] = x
            self.sizes[x] += self.sizes[y]

    def find(self, x):
        group = self.sets[x]
        while group != self.sets[group]:
            group = self.sets[group]
        self.sets[x] = group
        return group


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        primes = []
        for x in range(2, int(max(A) ** 0.5) + 1):
            for y in primes:
                if x % y == 0:
                    break
            else:
                primes.append(x)
        f = {}
        for a in A:
            factors = []
            _a = a
            for prime in primes:
                if prime * prime > a:
                    break
                if a % prime == 0:
                    factors.append(prime)
                while a % prime == 0:
                    a //= prime
            if a > 1:
                factors.append(a)
                primes.append(a)
            f[_a] = factors
        prime_lookup = {p: i for (i, p) in enumerate(primes)}
        dsu = DSU(len(primes))
        for (n, prime_factors) in list(f.items()):
            if prime_factors:
                p0 = prime_factors[0]
            for prime in prime_factors[1:]:
                dsu.union(prime_lookup[p0], prime_lookup[prime])
        counter = collections.Counter((dsu.find(prime_lookup[f[a][0]]) for a in A if f[a]))
        return max(counter.values())
