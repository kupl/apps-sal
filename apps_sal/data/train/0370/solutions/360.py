class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        fc = DisjointSetUnion(max(A))
        for a in A:
            for i in range(2, int(sqrt(a)) + 1):
                if a % i == 0:
                    fc.union(a, i)
                    fc.union(a, a // i)
        d = collections.defaultdict(int)
        maxlen = 0
        for a in A:
            group = fc.find(a)
            d[group] += 1
            maxlen = max(maxlen, d[group])
        return maxlen


class DisjointSetUnion(object):

    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px == py:
            return px
        if self.size[px] > self.size[py]:
            (px, py) = (py, px)
        self.parent[px] = py
        self.size[py] += self.size[px]
        return py
