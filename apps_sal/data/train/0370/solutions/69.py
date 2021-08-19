import math


class UnionFind:

    def __init__(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.uf[x_root] = y_root
        self.size[y_root] += self.size[x_root]
        self.size[x_root] = 0


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        d = {}
        uf = UnionFind(len(A))
        for (indx, num) in enumerate(A):
            primes = self.primeFactors(num)
            for prime in primes:
                if prime in d:
                    uf.union(indx, d[prime])
                d[prime] = indx
        return max(uf.size)

    def primeFactors(self, n):
        out = set()
        while n % 2 == 0:
            out.add(2)
            n /= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                out.add(i)
                n /= i
        if n > 2:
            out.add(n)
        return out
