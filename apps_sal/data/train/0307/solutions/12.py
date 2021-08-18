

class Solution:
    def soupServings(self, N: int) -> float:
        N = N // 25 + (N % 25 > 0)
        if N >= 500:
            return 1
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        operations = [(4, 0), (3, 1), (2, 2), (1, 3)]
        dp[-1][-1] = 1

        for i in range(N, 0, -1):
            for j in range(N, 0, -1):
                for a, b in operations:
                    if i - a < 0 and j - b < 0:
                        dp[0][0] += dp[i][j] * 0.25
                    elif i - a < 0:
                        dp[0][j - b] += dp[i][j] * 0.25
                    elif j - b < 0:
                        dp[i - a][0] += dp[i][j] * 0.25
                    else:
                        dp[i - a][j - b] += dp[i][j] * 0.25
        a_total = 0
        for i in range(N + 1):
            a_total += dp[0][i]

        return a_total - dp[0][0] / 2
