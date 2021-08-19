class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        face = len(rollMax)

        dp = [[0 for i in range(face + 1)] for j in range(n + 1)]

        # 0 roll
        dp[0][face] = 1
        # 1 roll
        for f in range(face):
            dp[1][f] = 1
        dp[1][face] = 6
        # 2 roll and more

        for i in range(2, n + 1):
            for j in range(face):
                for k in range(1, rollMax[j] + 1):
                    if (i - k) < 0:
                        break
                    dp[i][j] += dp[i - k][face] - dp[i - k][j]
            dp[i][face] = sum(dp[i])

        return dp[n][face] % 1000000007
