class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        m = len(grid)
        if m == 1:
            return False
        n = len(grid[0])
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def dfs(prev, curr):
            if curr in visited:
                return True
            visited.add(curr)
            for dirn in dirs:
                nei = (dirn[0] + curr[0], dirn[1] + curr[1])
                if 0 <= nei[0] < m and 0 <= nei[1] < n and (nei != prev) and (grid[nei[0]][nei[1]] == grid[curr[0]][curr[1]]):
                    if dfs(curr, nei):
                        return True
            return False
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if dfs(None, (i, j)):
                        return True
        return False
