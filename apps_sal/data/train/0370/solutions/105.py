class DSU:

    def __init__(self, N):
        self.p = list(range(N))
        self.sz = [1] * N
        self.max_sz = 1

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return self.p[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        if xr == yr:
            return
        if self.sz[xr] < self.sz[yr]:
            (x, y, xr, yr) = (y, x, yr, xr)
        self.p[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.max_sz = max(self.max_sz, self.sz[xr])


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def factorize(n):
            result = set()
            if n % 2 == 0:
                result.add(2)
                while n % 2 == 0:
                    n //= 2
            for i in range(3, int(sqrt(n)) + 1, 2):
                if n % i == 0:
                    result.add(i)
                    while n % i == 0:
                        n //= i
            if n > 1:
                result.add(n)
            return result
        if not A:
            return 0
        dsu = DSU(len(A))
        primes = dict()
        for (i, a) in enumerate(A):
            for prime in factorize(a):
                primes.setdefault(prime, []).append(i)
        for indices in primes.values():
            for i in range(len(indices) - 1):
                dsu.union(indices[i], indices[i + 1])
        return dsu.max_sz
