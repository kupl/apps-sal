class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        dp = piles.copy()
        for i in range(len(piles) - 2, -1, -1):
            for j in range(i + 1, len(piles)):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[len(dp) - 1] > 0
