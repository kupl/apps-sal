import math
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def prime_factorize(n):
            a = []
            while n % 2 == 0:
                a.append(2)
                n //= 2
            f = 3
            while f * f <= n:
                if n % f == 0:
                    a.append(f)
                    n //= f
                else:
                    f += 2
            if n != 1:
                a.append(n)
            return a

        uf = UnionFind(len(A))
        res = 0
        primes = defaultdict(list)
        
        for i, a in enumerate(A):
            for p in set(prime_factorize(a)):
                primes[p].append(i)

        for _, indices in primes.items():
            i0 = indices[0]
            for i1 in indices[1:]:
                uf.union(i0, i1)

        return -min(uf.parents)
