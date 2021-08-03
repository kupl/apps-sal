class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot != yroot:
            self.parent[yroot] = xroot


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = DSU()

        for i in range(n):
            for j in range(n):
                if i > 0:
                    dsu.union((i - 1, j, 2), (i, j, 0))
                if j > 0:
                    dsu.union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] != '/':
                    dsu.union((i, j, 0), (i, j, 1))
                    dsu.union((i, j, 2), (i, j, 3))
                if grid[i][j] != '\\\\':
                    dsu.union((i, j, 3), (i, j, 0))
                    dsu.union((i, j, 1), (i, j, 2))

        seen = set()
        for key in dsu.parent.keys():
            temp = dsu.find(key)
            seen.add(temp)

        return len(seen)
