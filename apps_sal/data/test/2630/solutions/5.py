class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        1 1 0
        1 1 0
        1 1 0
        """
        if not any(obstacleGrid):
            return 0

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1 if i == 0 or j == 0 else 1 for j in range(m)] for i in range(n)]

        # Set first column of dp.
        obs = False
        first_col = [i[0] for i in obstacleGrid]

        try:
            idx = first_col.index(1)
            for i in range(n):
                dp[i][0] = 1 if i < idx else 0
        except ValueError:
            pass

        # Set first row of dp.
        try:
            first_row = obstacleGrid[0]
            idx = first_row.index(1)
            dp[0] = [1] * idx + [0] * (m - idx)
        except ValueError:
            pass

        print(obstacleGrid)
        for i in range(1, n):
            for j in range(1, m):
                print(i, j)
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]
