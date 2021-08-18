class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        faces = len(rollMax)
        dp = [[0 for i in range(faces + 1)] for j in range(n + 1)]

        dp[0][faces] = 1
        for j in range(faces):
            dp[1][j] = 1
        dp[1][faces] = faces

        for i in range(2, n + 1):
            for j in range(faces):
                dp[i][j] = dp[i - 1][-1]
                if i - 1 - rollMax[j] >= 0:
                    dp[i][j] -= (dp[i - 1 - rollMax[j]][-1] - dp[i - 1 - rollMax[j]][j])
            dp[i][faces] = sum(dp[i])

        return dp[n][faces] % 1000000007
