class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for i in range(6)] for j in range(n)]
        for i in range(6):
            dp[0][i] = 1
        for i in range(1, n):
            total = sum(dp[i - 1])
            for j in range(6):
                dp[i][j] += total
                if i - rollMax[j] == 0:
                    dp[i][j] -= 1
                if i - rollMax[j] > 0:
                    dp[i][j] -= sum(dp[i - rollMax[j] - 1]) - dp[i - rollMax[j] - 1][j]
        return sum(dp[n - 1]) % (10**9 + 7)
