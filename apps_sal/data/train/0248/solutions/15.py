class DSU:
    def __init__(self):
        self.reps = {}

    def add(self, x):
        self.reps[x] = x

    def find(self, x):
        if not x == self.reps[x]:
            self.reps[x] = self.find(self.reps[x])
        return self.reps[x]

    def union(self, x, y):
        self.reps[self.find(y)] = self.find(x)


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        dsu = DSU()
        for i in range(m):
            for j in range(n):
                dsu.add((i, j))
                if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j] == grid[i][j - 1] == grid[i][j] and dsu.find((i - 1, j)) == dsu.find((i, j - 1)):
                    return True
                if i - 1 >= 0 and grid[i - 1][j] == grid[i][j]:
                    dsu.union((i - 1, j), (i, j))
                if j - 1 >= 0 and grid[i][j - 1] == grid[i][j]:
                    dsu.union((i, j - 1), (i, j))
        return False
