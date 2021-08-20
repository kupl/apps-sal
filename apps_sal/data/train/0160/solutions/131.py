from functools import lru_cache


class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = piles[:]
        for d in range(1, N):
            for i in range(N - d):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + d] - dp[i])
        return dp[0] > 0
