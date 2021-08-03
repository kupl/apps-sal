class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        dp = [0 for _ in range(col)]
        dp[0] = grid[0][0]

        for i in range(1, col):
            dp[i] = dp[i - 1] + grid[0][i]

        for i in range(1, row):
            for j in range(0, col):
                dp[j] = dp[j] + grid[i][j] if j == 0 else min(dp[j - 1], dp[j]) + grid[i][j]

        return dp[-1]
