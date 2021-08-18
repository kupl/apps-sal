

class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        p = piles
        n = len(p)

        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = p[i]

        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])

        return dp[0][-1] > 0


class Solution:
    def stoneGame(self, p):
        n = len(p)
        dp = p[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
        return dp[0] > 0
