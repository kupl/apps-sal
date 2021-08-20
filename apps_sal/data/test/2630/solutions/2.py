class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        if obstacleGrid[-1][-1] == 1:
            return 0
        dp = []
        for each in obstacleGrid:
            temp = each[:]
            dp.append(temp)
        for i in range(len(dp[0])):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1
        for j in range(len(dp)):
            if obstacleGrid[j][0] == 1:
                break
            else:
                dp[j][0] = 1
        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 0:
                    if obstacleGrid[row - 1][col] != 1:
                        dp[row][col] += dp[row - 1][col]
                    if obstacleGrid[row][col - 1] != 1:
                        dp[row][col] += dp[row][col - 1]
        print(dp)
        return dp[-1][-1]
