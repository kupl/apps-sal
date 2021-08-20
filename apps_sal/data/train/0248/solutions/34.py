import sys
input = sys.stdin.readline


class Unionfind:

    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [1] * n

    def root(self, x):
        r = x
        while not self.par[r] < 0:
            r = self.par[r]
        t = x
        while t != r:
            tmp = t
            t = self.par[t]
            self.par[tmp] = r
        return r

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if self.rank[rx] <= self.rank[ry]:
            self.par[ry] += self.par[rx]
            self.par[rx] = ry
            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] += 1
        else:
            self.par[rx] += self.par[ry]
            self.par[ry] = rx

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def count(self, x):
        return -self.par[self.root(x)]


class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        uf = Unionfind(n * m)
        for i in range(n):
            for j in range(m):
                if i + 1 < n and grid[i][j] == grid[i + 1][j]:
                    if uf.is_same(m * i + j, m * (i + 1) + j):
                        return True
                    uf.unite(m * i + j, m * (i + 1) + j)
                if j + 1 < m and grid[i][j] == grid[i][j + 1]:
                    if uf.is_same(m * i + j, m * i + j + 1):
                        return True
                    uf.unite(m * i + j, m * i + j + 1)
        return False
