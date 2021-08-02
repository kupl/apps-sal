class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n  # 这里先填充了0，这样当i==0时也可以dp[j] += dp[j-1]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:  # 遇到障碍物直接为0
                    dp[j] = 0
                else:  # 没有遇到障碍物
                    if i == 0 and j == 0:  # 左上角总是为1，也为后面i!=0而j==0的情况做铺垫
                        dp[j] = 1
                    elif j != 0:  # 因为j==0时，应该为dp[j] += 0，等于不变，所以continue
                        dp[j] += dp[j - 1]
        return dp[-1]
