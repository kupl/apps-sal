class Solution:

    def regionsBySlashes(self, g: List[str]) -> int:
        n = len(g)
        grid = [[0] * (n * 3) for j in range(n * 3)]
        for i in range(n):
            for j in range(n):
                if g[i][j] == '/':
                    grid[i * 3][j * 3 + 2] = 1
                    grid[i * 3 + 1][j * 3 + 1] = 1
                    grid[i * 3 + 2][j * 3] = 1
                elif g[i][j] == '\\\\':
                    grid[i * 3][j * 3] = 1
                    grid[i * 3 + 1][j * 3 + 1] = 1
                    grid[i * 3 + 2][j * 3 + 2] = 1

        def dfs(i, j):
            grid[i][j] = 1
            for r in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                (xx, yy) = r
                if xx < 0 or yy < 0 or xx >= len(grid) or (yy >= len(grid[0])) or (grid[xx][yy] == 1):
                    continue
                dfs(xx, yy)
        count = 0
        for i in range(n * 3):
            for j in range(n * 3):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        return count
