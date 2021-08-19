class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        if n == 1:
            return True
        dp = [[None] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n - 1] > 0
