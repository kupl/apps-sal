class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        for j in range(m):
            if obstacleGrid[j][0] == 0:
                dp[j][0] = 1
            else:
                break

        if obstacleGrid[m - 1][n - 1] == 1:
            return 0

        print(dp)

        for y in range(1, n):
            for x in range(1, m):
                if obstacleGrid[x][y] == 1:
                    dp[x][y] = 0
                else:
                    dp[x][y] = dp[x - 1][y] + dp[x][y - 1]

        return dp[m - 1][n - 1]
