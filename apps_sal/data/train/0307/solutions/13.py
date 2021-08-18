class Solution:
    def soupServings(self, N: int) -> float:
        n = N // 25 + (N % 25 > 0)
        if n >= 500:
            return 1
        dp = [[0] * (n + 1) for i in range(n + 1)]
        dp[-1][-1] = 1

        x = [-4, -3, -2, -1]
        y = [0, -1, -2, -3]
        for i in range(n, 0, -1):
            for j in range(n, 0, -1):
                for dx, dy in zip(x, y):
                    if i + dx < 0 and j + dy < 0:
                        dp[0][0] += dp[i][j] * (0.25)
                    elif i + dx < 0:
                        dp[0][j + dy] += dp[i][j] * (0.25)
                    elif j + dy < 0:
                        dp[i + dx][0] += dp[i][j] * (0.25)
                    else:
                        dp[i + dx][j + dy] += dp[i][j] * (0.25)

        Sum = 0
        for j in range(n + 1):
            Sum += dp[0][j]

        return Sum - dp[0][0] / 2
