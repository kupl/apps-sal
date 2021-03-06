class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 7 for _ in range(n + 1)]
        for j in range(1, 7):
            dp[1][j] = 1
        dp[0][0] = 1
        dp[1][0] = 6
        for i in range(2, n + 1):
            for j in range(1, 7):
                for k in range(1, min(i, rollMax[j - 1]) + 1):
                    dp[i][j] = sumMod(dp[i][j], dp[i - k][0] - dp[i - k][j])
                dp[i][0] = sumMod(dp[i][0], dp[i][j])
        return dp[n][0]


def sumMod(x: int, y: int) -> int:
    return (x + y) % (10 ** 9 + 7)
