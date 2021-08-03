class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [0] * n
        dp[n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                if i == m - 1:
                    dp[j] = max(1, dp[j + 1] - dungeon[i][j])
                elif j == n - 1:
                    dp[j] = max(1, dp[j] - dungeon[i][j])
                else:
                    dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])
        return dp[0]
