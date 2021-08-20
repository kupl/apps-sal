class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[None for _ in range(n)] for _ in range(n)]
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                if j == i + 1:
                    dp[i][j] = abs(piles[i] - piles[j])
                else:
                    dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n - 1] > 0
