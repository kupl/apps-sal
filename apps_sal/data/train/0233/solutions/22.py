class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        if not grid:
            return 0
        (rows, cols) = (len(grid), len(grid[0]))
        new_grid = [[0] * 3 * cols for _ in range(3 * rows)]
        visited = [[False] * 3 * cols for _ in range(3 * rows)]
        for i in range(rows):
            line = grid[i]
            for j in range(len(line)):
                if line[j] == '/':
                    new_grid[3 * i][3 * j + 2] = 1
                    new_grid[3 * i + 1][3 * j + 1] = 1
                    new_grid[3 * i + 2][3 * j] = 1
                elif line[j] == '\\\\':
                    new_grid[3 * i][3 * j] = 1
                    new_grid[3 * i + 1][3 * j + 1] = 1
                    new_grid[3 * i + 2][3 * j + 2] = 1

        def dfs(i, j):
            if i < 0 or j < 0 or i >= 3 * rows or (j >= 3 * cols) or (new_grid[i][j] == 1) or visited[i][j]:
                return
            visited[i][j] = True
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)
        count = 0
        for i in range(3 * rows):
            for j in range(3 * cols):
                if not visited[i][j] and new_grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        return count
