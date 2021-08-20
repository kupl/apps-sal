class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        faces = len(rollMax)
        dp = [[0] * (faces + 1) for _ in range(n + 1)]
        dp[0][faces] = 1
        for j in range(faces):
            dp[1][j] = 1
        dp[1][faces] = faces
        for i in range(2, n + 1):
            for j in range(faces):
                k = 1
                while k <= i and k <= rollMax[j]:
                    dp[i][j] += dp[i - k][faces] - dp[i - k][j]
                    k += 1
            dp[i][faces] = sum(dp[i])
        return dp[n][faces] % 1000000007
