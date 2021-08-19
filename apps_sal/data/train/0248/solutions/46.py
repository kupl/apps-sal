class Solution:

    def containsCycle(self, grid) -> bool:
        if not grid or not grid[0]:
            return False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * len(grid[i]) for i in range(len(grid))]

        def dfs(grid, symbol, row, col, prev_row, prev_col):
            nonlocal directions
            nonlocal visited
            visited[row][col] = True
            for direction in directions:
                nr = row + direction[0]
                nc = col + direction[1]
                if nr == prev_row and nc == prev_col:
                    continue
                if len(grid) > nr >= 0 and len(grid[nr]) > nc >= 0:
                    if grid[nr][nc] == symbol and (visited[nr][nc] or dfs(grid, symbol, nr, nc, row, col)):
                        return True
            return False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j]:
                    if dfs(grid, grid[i][j], i, j, 0, 0):
                        return True
        return False
