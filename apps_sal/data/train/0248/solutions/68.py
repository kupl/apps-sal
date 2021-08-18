class UF:
    def __init__(self, m, n):
        self.p = {(i, j): (i, j) for i in range(m) for j in range(n)}

    def union(self, ti, tj):
        pi, pj = self.find(*ti), self.find(*tj)
        if pi != pj:
            self.p[pj] = pi
            return False
        return True

    def find(self, i, j):
        if (i, j) != self.p[i, j]:
            self.p[i, j] = self.find(*self.p[i, j])
        return self.p[i, j]


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UF(m, n)
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if uf.union(tuple([i - 1, j]), tuple([i, j])):
                        return True
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if uf.union(tuple([i, j - 1]), tuple([i, j])):
                        return True
        return False
