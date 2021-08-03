class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 7 for _ in range(n + 1)]
        ans = 1
        for i in range(1, n + 1):
            temp = 0
            for j, r in enumerate(rollMax):
                if i - r > 1:
                    dp[i][j] = ans - dp[i - r - 1][-1] + dp[i - r - 1][j]
                elif i - r == 1:
                    dp[i][j] = ans - 1
                else:
                    dp[i][j] = ans
                temp += dp[i][j]
            dp[i][-1] = temp
            ans = temp
        # print(sum(dp[4]))
        # print(dp)
        return temp % int(1e9 + 7)
#         dp = [[0] * (len(rollMax) + 1) for _ in range(n + 1)]
#         for j in range(len(rollMax)):
#             dp[1][j] = 1
#             dp[1][-1] += dp[1][j]

#         for i in range(2, n + 1):
#             for j in range(len(rollMax)):
#                 dp[i][j] = dp[i - 1][-1]
#                 k = i - rollMax[j]
#                 if k == 1:
#                     dp[i][j] -= 1
#                 elif k > 1:
#                     dp[i][j] -= (dp[k - 1][-1] - dp[k - 1][j])
#                 dp[i][-1] += dp[i][j]
#         print(dp)
#         return dp[n][len(rollMax)] % int(1e9 + 7)
# [[0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 6], [5, 5, 5, 6, 6, 6, 33], [28, 28, 28, 32, 32, 33, 181], [153, 153, 153, 176, 176, 180, 991], [838, 838, 838, 964, 964, 986, 5428]]
