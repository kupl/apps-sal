class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        (n, m) = (len(grid), len(grid[0]))
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(i, j, pre_i, pre_j):
            visited.add((i, j))
            for (x, y) in directions:
                if 0 <= x + i < n and 0 <= y + j < m and (grid[i][j] == grid[i + x][j + y]) and (i + x != pre_i or j + y != pre_j):
                    if (i + x, j + y) in visited or dfs(i + x, j + y, i, j):
                        return True
            return False
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited:
                    if dfs(i, j, -1, -1):
                        return True
        return False
