class Solution:
    def find(self, n1):
        if n1 == self.par[n1[0]][n1[1]]:
            return n1
        else:
            return self.find(self.par[n1[0]][n1[1]])

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        self.par[p1[0]][p1[1]] = p2

    def containsCycle(self, grid: List[List[str]]) -> bool:
        n_row, n_col = len(grid), len(grid[0])
        self.par = []
        for r in range(n_row):
            self.par.append([(r, c) for c in range(n_col)])

        for r in range(n_row):
            for c in range(n_col):
                if r + 1 < n_row and grid[r][c] == grid[r + 1][c]:
                    if self.find((r, c)) == self.find((r + 1, c)):
                        return True
                    self.union((r, c), (r + 1, c))
                if c + 1 < n_col and grid[r][c] == grid[r][c + 1]:
                    if self.find((r, c)) == self.find((r, c + 1)):
                        return True
                    self.union((r, c), (r, c + 1))

        return False
