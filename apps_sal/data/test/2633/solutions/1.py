class Solution:

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        (M, N) = (len(dungeon), len(dungeon[0]))
        dp = [[0] * N for _ in range(M)]
        for i in reversed(list(range(M))):
            for j in reversed(list(range(N))):
                v = dungeon[i][j]
                if i == M - 1 and j == N - 1:
                    dp[i][j] = 1 - v
                elif i == M - 1:
                    dp[i][j] = dp[i][j + 1] - v
                elif j == N - 1:
                    dp[i][j] = dp[i + 1][j] - v
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - v
                dp[i][j] = max(1, dp[i][j])
        return dp[0][0]
