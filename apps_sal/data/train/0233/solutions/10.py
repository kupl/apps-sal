class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        new_grid = [[0] * (2 * N) for _ in range(2 * N)]
        count = 0

        for i in range(N):
            for j in range(N):
                if grid[i][j] == '/':
                    new_grid[2 * i][2 * j + 1] = 1
                    new_grid[2 * i + 1][2 * j] = 1
                elif grid[i][j] == '\\\\':
                    new_grid[2 * i][2 * j] = 1
                    new_grid[2 * i + 1][2 * j + 1] = 1

        def dfs(grid, i, j):
            if grid[i][j] == 1:
                return None
            grid[i][j] = 1
            if i < len(grid) - 1:
                dfs(grid, i + 1, j)
            if j < len(grid) - 1:
                dfs(grid, i, j + 1)
            if i > 0:
                dfs(grid, i - 1, j)
            if j > 0:
                dfs(grid, i, j - 1)
            if i < len(grid) - 1 and j > 0 and i % 2 == j % 2:
                dfs(grid, i + 1, j - 1)
            if i > 0 and j < len(grid) - 1 and i % 2 == j % 2:
                dfs(grid, i - 1, j + 1)
            if i < len(grid) - 1 and j < len(grid) - 1 and i % 2 != j % 2:
                dfs(grid, i + 1, j + 1)
            if i > 0 and j > 0 and i % 2 != j % 2:
                dfs(grid, i - 1, j - 1)

        for i in range(2 * N):
            for j in range(2 * N):
                if new_grid[i][j] == 0:
                    count += 1
                    dfs(new_grid, i, j)

        return count
