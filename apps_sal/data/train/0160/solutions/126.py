class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        if n == 1:
            return True

        dp = piles[:]
        for l in range(1, n):
            for i in range(n - l - 1, -1, -1):
                j = i + l
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])

        return dp[-1] > 0
