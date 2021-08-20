class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif i == 0 and j == 0:
                    dp[j] = 1
                elif j != 0:
                    dp[j] += dp[j - 1]
        return dp[-1]
