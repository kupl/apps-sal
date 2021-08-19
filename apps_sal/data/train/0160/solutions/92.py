class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[None] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = [piles[i], 0]
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                first = max(piles[i] + dp[i + 1][j][1], piles[j] + dp[i][j - 1][1])
                second = min(dp[i + 1][j][0], dp[i][j - 1][0])
                dp[i][j] = [first, second]
        return dp[0][-1][0] > dp[0][-1][1]
