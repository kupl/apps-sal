class Solution:

    def stoneGame(self, piles):
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        presum = [0]
        for p in piles:
            presum.append(p + presum[-1])
        for i in range(n):
            dp[i][i] = piles[i]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] + presum[j + 1] - presum[i + 1] - dp[i + 1][j], piles[j] + presum[j] - presum[i] - dp[i][j - 1])
        return dp[0][n - 1] > presum[-1] - dp[0][n - 1]
