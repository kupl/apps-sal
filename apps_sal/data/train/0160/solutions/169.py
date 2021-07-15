class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for i in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]
        
        for d in range(1, n + 1):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])
        
        return dp[0][-1] > 0
