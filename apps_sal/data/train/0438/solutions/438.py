class DSU:

    def __init__(self, m):
        self.p = {}
        self.islands = {}
        self.m = m
        self.hasm = 0

    def make_island(self, x):
        self.p[x] = x
        self.islands[x] = 1
        if self.m == 1:
            self.hasm += 1

    def exist(self, x):
        if not x in self.p:
            return False
        return True

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        if not self.exist(x) or not self.exist(y):
            return
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        if self.islands[yr] == self.m:
            self.hasm -= 1
        if self.islands[xr] == self.m:
            self.hasm -= 1
        self.islands[yr] = self.islands[xr] + self.islands[yr]
        if self.islands[yr] == self.m:
            self.hasm += 1
        del self.islands[xr]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -1
        dsu = DSU(m)
        for (i, x) in enumerate(arr):
            if not dsu.exist(x):
                dsu.make_island(x)
                dsu.union(x, x + 1)
                dsu.union(x, x - 1)
                if dsu.hasm != 0:
                    res = i + 1
        return res
