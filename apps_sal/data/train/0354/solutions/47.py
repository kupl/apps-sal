class Solution:
    def dieSimulator(self, n, rollMax):
        mod = 10**9 + 7
        dp = [[0, 1] + [0] * 15 for i in range(6)]
        for _ in range(n - 1):
            dp2 = [[0] * 17 for i in range(6)]
            for i in range(6):
                for k in range(1, rollMax[i] + 1):
                    for j in range(6):
                        if i == j:
                            if k < rollMax[i]:
                                dp2[j][k + 1] += dp[i][k] % mod
                        else:
                            dp2[j][1] += dp[i][k] % mod
            dp = dp2
        return sum(sum(row) for row in dp) % mod
#     def dieSimulator(self, n: int, rollMax: List[int]) -> int:
#         faces = len(rollMax)
#         # [n + 1][faces + 1] dimensional dp array
#         dp = [[0 for i in range(faces + 1)] for j in range(n + 1)]
        
#         # initialization
#         # roll 0 times, the total combination is 1
#         dp[0][faces] = 1
#         # roll 1 times, the combinations that end at face j is 1
#         for j in range(faces):
#             dp[1][j] = 1
#         # roll 1 times, the total combination is faces = 6
#         dp[1][faces] = faces
        
#         # then roll dices from 2 times, until n times
#         for i in range(2, n + 1):
#             # iterate through each column (face)
#             for j in range(faces):
#                 # at each [i, j], trying to go up (decrease i) and collect all the sum of previous state
#                 dp[i][j] = dp[i-1][faces]
#                 if i-1-rollMax[j] >= 0:
#                     dp[i][j] -= (dp[i-1-rollMax[j]][faces] - dp[i-1-rollMax[j]][j])
#             # update total sum of this row
#             dp[i][faces] = sum(dp[i])
        
#         return dp[n][faces] % 1000000007

