import math
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return px
        if self.size[px] > self.size[py]:
            px, py = py, px
        self.parent[px] = py
        self.size[py] += self.size[px]
        return py


class Solution:
    def largestComponentSize(self, A: list()) -> int:
        n = max(A)
        n_UnionFind = UnionFind(n + 1)
        for a in A:
            for k in range(2, int(math.sqrt(a)) + 1):
                if a % k == 0:
                    n_UnionFind.union(a, k)
                    n_UnionFind.union(a, a // k)
        ans = 1
        count = defaultdict(int)
        for a in A:
            count[n_UnionFind.find(a)] += 1
            ans = max(ans, count[n_UnionFind.find(a)])
        return ans
