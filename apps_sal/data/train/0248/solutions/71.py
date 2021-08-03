class Solution:
    def rec(self, i, j, char, prev):
        if self.grid[i][j] != char:
            return False
        if self.matrix[i][j]:
            return True
        else:
            self.matrix[i][j] = True

        l = (i, j - 1)
        r = (i, j + 1)
        u = (i - 1, j)
        d = (i + 1, j)

        for c in [l, r, u, d]:
            if 0 <= c[0] < self.row and 0 <= c[1] < self.col and c != prev:
                if self.rec(c[0], c[1], char, (i, j)):
                    return True
        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])

        self.matrix = [[False for i in range(self.col)] for j in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):
                if not self.matrix[i][j]:
                    if self.rec(i, j, grid[i][j], 0):
                        return True
        return False
