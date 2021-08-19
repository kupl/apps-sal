import collections


class Solution:

    def findLatestStep(self, placed, target):
        N = len(placed)
        A = [0] * N
        dsu = DSU(N)
        sizes = collections.Counter()
        ans = -1
        for (i, x) in enumerate(placed, 1):
            x -= 1
            A[x] = 1
            for y in (x - 1, x + 1):
                if 0 <= y < N and A[y]:
                    sizes[dsu.size(y)] -= 1
                    dsu.union(x, y)
            sizes[dsu.size(x)] += 1
            if sizes[target] > 0:
                ans = i
        return ans


class DSU:

    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            (xr, yr) = (yr, xr)
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.sz[yr] = self.sz[xr]
        return True

    def size(self, x):
        return self.sz[self.find(x)]
