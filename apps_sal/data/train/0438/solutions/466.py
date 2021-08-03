class DSU:

    def __init__(self, n, m):
        self.parents = [-1] * n
        self.sizes = [0] * n
        self.target = m
        self.matches = 0

    def find(self, x):
        parent = self.parents[x]
        if parent in [-1, x]:
            return parent
        self.parents[x] = self.find(parent)
        return self.parents[x]

    def union(self, x, y):
        if x == y:
            self.parents[x] = x
            self.sizes[x] = 1
            if 1 == self.target:
                self.matches += 1
        else:
            px, py = self.find(x), self.find(y)
            sx, sy = self.sizes[px], self.sizes[py]
            if sy > sx:
                px, py = py, px
                sx, sy = sy, sx
            self.parents[py] = px
            self.sizes[px] = sx + sy
            if sx == self.target:
                self.matches -= 1
            if sy == self.target:
                self.matches -= 1
            if sx + sy == self.target:
                self.matches += 1


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        dsu = DSU(len(arr), m)
        last_good = -1
        for i, v in enumerate(arr):
            v -= 1
            dsu.union(v, v)
            if v - 1 >= 0 and dsu.find(v - 1) != -1:
                dsu.union(v, v - 1)
            if v + 1 < len(arr) and dsu.find(v + 1) != -1:
                dsu.union(v, v + 1)
            if dsu.matches > 0:
                last_good = i + 1
        return last_good
