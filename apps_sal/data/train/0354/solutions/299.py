class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        for j = 0, 1, ..., faces - 1
        dp[i][j] means how many combinations it could be that at i-th rolling and the last face is j
        for j = faces
        dp[i][j] means how many combinations in total with i rollings

        """
        faces = len(rollMax)
        dp = [[0 for _ in range(faces + 1)] for _ in range(n + 1)]
        dp[0][faces] = 1
        for j in range(faces):
            dp[1][j] = 1
        dp[1][faces] = faces
        for i in range(2, n + 1):
            for j in range(faces):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i - k][faces] - dp[i - k][j]
            dp[i][faces] = sum(dp[i])
        return dp[n][faces] % 1000000007
