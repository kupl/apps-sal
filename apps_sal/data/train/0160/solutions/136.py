class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = piles[i]
        for d in range(1, N):
            for i in range(N - d):
                j = d + i
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][-1] > 0
