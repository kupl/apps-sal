class Solution:
    f = {}

    def find(self, x):
        self.f.setdefault(x, x)
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        self.f[self.find(x)] = self.find(y)

    def regionsBySlashes(self, grid: List[str]) -> int:
        self.f = {}
        for row in range(len(grid)):
            for col in range(len(grid)):
                if row:
                    self.union((row - 1, col, 2), (row, col, 0))
                if col:
                    self.union((row, col - 1, 3), (row, col, 1))
                if grid[row][col] != '/':
                    self.union((row, col, 0), (row, col, 3))
                    self.union((row, col, 1), (row, col, 2))
                if grid[row][col] != '\\\\':
                    self.union((row, col, 0), (row, col, 1))
                    self.union((row, col, 2), (row, col, 3))
        return len(set(map(self.find, self.f)))
