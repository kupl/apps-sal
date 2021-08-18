class Solution:
    def stoneGame(self, p: List[int]) -> bool:
        n = len(p)
        dp = [[int(j == i) for j in range(n)] for i in range(n)]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0
