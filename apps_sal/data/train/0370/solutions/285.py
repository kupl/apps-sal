class DisjointSetUnion():
    def __init__(self, size):
        self.parents = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        # x and y are in the same set
        if px == py:
            return px
        if self.size[px] > self.size[py]:
            px, py = py, px
        self.parents[px] = py
        self.size[py] += self.size[px]
        return py

import math
from collections import defaultdict
class Solution:
    def largestComponentSize(self, A) -> int:
        dsu = DisjointSetUnion(max(A))
        for a in A:
            for factor in range(2, int(math.sqrt(a)) + 1):
                if a % factor == 0:
                    dsu.union(a, factor)
                    dsu.union(a, a // factor)
        max_size = 0
        group_count = defaultdict(int)
        for a in A:
            idx = dsu.find(a)
            group_count[idx] += 1
            max_size = max(max_size, group_count[idx])
        return max_size
