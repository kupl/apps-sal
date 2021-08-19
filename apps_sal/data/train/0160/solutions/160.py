class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for i in range(n)] for j in range(n)]
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if l % 2 == 0:
                    dp[i][j] = max(dp[i + 1][j] + piles[i], dp[i][j - 1] + piles[j])
                else:
                    dp[i][j] = min(dp[i + 1][j] - piles[i], dp[i][j - 1] - piles[j])
        return dp[0][n - 1] > 0
