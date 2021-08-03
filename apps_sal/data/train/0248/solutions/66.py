class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dsu = DSU()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i != 0 and grid[i - 1][j] == grid[i][j]:
                    dsu.union((i - 1, j), (i, j))
                if grid[i][j - 1] == grid[i][j]:
                    if dsu.find((i, j - 1)) == dsu.find((i, j)):
                        return True
                    dsu.union((i, j - 1), (i, j))
        return False


class DSU:
    def __init__(self):
        self.father = {}

    def find(self, a):
        self.father.setdefault(a, a)
        if a != self.father[a]:
            self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        _a = self.find(a)
        _b = self.find(b)
        if _a != _b:
            self.father[_a] = self.father[_b]
