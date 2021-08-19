class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        if m == 1 or n == 1:
            return False
        dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def dfs(prev, curr):
            if curr in visited:
                return True
            visited.add(curr)
            for d in dir:
                x = (curr[0] + d[0], curr[1] + d[1])
                if x != prev and 0 <= x[0] < m and (0 <= x[1] < n) and (grid[x[0]][x[1]] == grid[curr[0]][curr[1]]):
                    if dfs(curr, x):
                        return True
            else:
                return False
        for i in range(m):
            for j in range(n):
                node = (i, j)
                if node not in visited:
                    if dfs(None, node) == True:
                        return True
        return False
