class Solution:

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [grid[0][j] for j in range(n)]
        for j in range(1, n):
            dp[j] += dp[j - 1]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(grid[i][j] + dp[j - 1], grid[i][j] + dp[j])
        return dp[-1]
