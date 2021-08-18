class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [piles[0]] * n
        for j in range(1, n):
            dp[j] = piles[j]
            for i in range(j - 1, -1, -1):
                dp[i] = max(piles[i] - dp[i + 1], piles[j] - dp[i])

        return dp[0] > 0
