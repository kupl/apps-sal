class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        dsu = DUS()
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if j != 0 and grid[i][j] == grid[i][j - 1]:
                    dsu.union((i, j), (i, j - 1))

                if i != 0 and grid[i][j] == grid[i - 1][j]:
                    if dsu.find((i, j)) == dsu.find((i - 1, j)):
                        return True
                    dsu.union((i, j), (i - 1, j))
        return False


class DUS:
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
            self.father[_a] = _b
