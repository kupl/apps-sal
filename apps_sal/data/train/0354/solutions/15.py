class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        faces = len(rollMax)
        dp = [[0 for i in range(faces + 1)] for j in range(n + 1)]

        dp[0][faces] = 1
        for j in range(faces):
            dp[1][j] = 1
        dp[1][faces] = faces

        for i in range(2, n + 1):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i - k][faces] - dp[i - k][j]
            dp[i][faces] = sum(dp[i])

        return dp[n][faces] % 1000000007
