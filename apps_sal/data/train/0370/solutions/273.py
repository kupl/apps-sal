import collections


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.ranks = [0 for _ in range(n)]

    def get_root(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.get_root(self.parents[x])
        return self.parents[x]

    def merge(self, x, y):
        x = self.get_root(x)
        y = self.get_root(y)
        if x != y:
            if self.ranks[x] < self.ranks[y]:
                self.parents[x] = y
            else:
                self.parents[y] = x
                if self.ranks[x] == self.ranks[y]:
                    self.ranks[x] += 1


def factorize_all(n):
    factorizations = [None] * (n + 1)
    factorizations[0] = {}
    factorizations[1] = {}
    for p in range(2, n + 1):
        if factorizations[p] is None:
            for k in range(1, n // p + 1):
                if factorizations[k] is None:
                    continue
                fs = factorizations[k].copy()
                if p in fs:
                    fs[p] += 1
                else:
                    fs[p] = 1
                factorizations[k * p] = fs
    return factorizations


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(max(A) + 1)
        factorization = factorize_all(max(A))
        ids = dict()
        for a in A:
            if a < 2:
                continue
            factors = list(factorization[a].keys())
            ids[a] = factors[0]
            for p0, p1 in zip(factors, factors[1:]):
                uf.merge(p0, p1)
                
        counter = collections.defaultdict(int)
        maxval = 0
        for a in A:
            if a < 2:
                continue
            id_ = uf.get_root(ids[a])
            counter[id_] += 1
            maxval = max(maxval, counter[id_])
            
        return maxval
