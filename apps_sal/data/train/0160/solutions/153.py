from functools import lru_cache


class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = [[0] * N for i in range(N)]
        for i in range(N):
            dp[i][i] = piles[i]
        for d in range(1, N):
            for i in range(N - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0
