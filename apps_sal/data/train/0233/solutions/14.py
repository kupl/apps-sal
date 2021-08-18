class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        self.N = len(grid)
        print((self.N))
        pre = list(range(self.N * self.N * 4))
        self.count = self.N * self.N * 4
        for r in range(self.N):
            line = grid[r]
            for c in range(self.N):
                w = line[c]
                if r > 0:
                    self.union(pre, self.g(r - 1, c, 2), self.g(r, c, 0))
                if c > 0:
                    self.union(pre, self.g(r, c - 1, 1), self.g(r, c, 3))
                if w != '/':
                    self.union(pre, self.g(r, c, 0), self.g(r, c, 1))
                    self.union(pre, self.g(r, c, 3), self.g(r, c, 2))
                if w != '\\\\':
                    self.union(pre, self.g(r, c, 0), self.g(r, c, 3))
                    self.union(pre, self.g(r, c, 1), self.g(r, c, 2))
        return self.count

    def find(self, pre, x):
        if x == pre[x]:
            return x

        return self.find(pre, pre[x])

    def union(self, pre, a, b):
        pa = self.find(pre, a)
        pb = self.find(pre, b)
        if (pa == pb):
            return
        pre[pa] = pb
        self.count -= 1

    def g(self, r, c, i):
        return (r * self.N + c) * 4 + i
