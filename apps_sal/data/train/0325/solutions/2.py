class Solution:

    def maxDistance(self, grid: List[List[int]]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        dp = [[math.inf] * n for _ in range(m)]
        land = water = 0
        for (i, row) in enumerate(grid):
            for (j, cell) in enumerate(row):
                if cell:
                    dp[i][j] = 0
                    land += 1
                else:
                    water += 1
        if not land or not water:
            return -1

        def process(dp):
            for i in range(m):
                for j in range(n):
                    if i:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                    if j:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        process(dp)
        dp = dp[::-1]
        process(dp)
        dp = [row[::-1] for row in dp]
        process(dp)
        dp = dp[::-1]
        process(dp)
        return max((max(row) for row in dp))
