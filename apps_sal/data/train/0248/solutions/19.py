class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        (m, n) = (len(grid), len(grid[0]))
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        visited = [[False] * n for i in range(m)]

        def dfs(y, x, py, px, c):
            visited[y][x] = True
            for d in dirs:
                (ny, nx) = (y + d[0], x + d[1])
                if ny < 0 or ny >= m or nx < 0 or (nx >= n) or (ny == py and nx == px) or (grid[ny][nx] != c):
                    continue
                if visited[ny][nx] or dfs(ny, nx, y, x, c):
                    return True
            return False
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and dfs(i, j, -1, -1, grid[i][j]):
                    return True
        return False
