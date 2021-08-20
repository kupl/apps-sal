class Solution:

    def primeFactors(self, n):
        pset = set()
        while n % 2 == 0:
            pset.add(2)
            n = n // 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                pset.add(i)
                n = n // i
        if n > 2:
            pset.add(n)
        return pset

    def largestComponentSize(self, A: List[int]) -> int:
        ds = DisjointSet(A)
        primeRoots = {}
        for (i, a) in enumerate(A):
            primes = self.primeFactors(a)
            for p in primes:
                if p in primeRoots:
                    ds.union(i, primeRoots[p])
                primeRoots[p] = i
        return max(ds.sizes)


class DisjointSet:

    def __init__(self, elements):
        self.parents = [x for x in range(len(elements))]
        self.sizes = [1] * len(elements)

    def find(self, x):
        while x != self.parents[x]:
            (x, self.parents[x]) = (self.parents[x], self.parents[self.parents[x]])
        return x

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px == py:
            return px
        if self.sizes[px] > self.sizes[py]:
            (py, px) = (px, py)
        self.parents[px] = py
        self.sizes[py] += self.sizes[px]
