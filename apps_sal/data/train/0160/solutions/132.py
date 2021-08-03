class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = piles[i]
        for i in range(N):
            for j in range(i + 1, N):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

        return dp[i][-1] > 0
