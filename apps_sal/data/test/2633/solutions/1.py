class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        # sol1: DP, choose the safest path
        # http://leetcodesolution.blogspot.kr/2015/01/leetcode-dungeon-game.html
        # minInitHealth[i][j] = min(minInitHealth[i+1][j], minInitHealth[i][j+1]) - dungeon[i][j]
        # set minInitHealth[i][j] to 1 if < 1
        M, N = len(dungeon), len(dungeon[0])
        dp = [[0] * N for _ in range(M)]
        for i in reversed(list(range(M))):
            for j in reversed(list(range(N))):
                v = dungeon[i][j]
                # choose right/down, which requires less
                if i == M - 1 and j == N - 1:
                    dp[i][j] = 1 - v
                elif i == M - 1:
                    dp[i][j] = dp[i][j + 1] - v
                elif j == N - 1:
                    dp[i][j] = dp[i + 1][j] - v
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - v
                # always ensure >= 1
                dp[i][j] = max(1, dp[i][j])
        return dp[0][0]
