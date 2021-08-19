class Solution:
    def numRollsToTarget(self, d, f, target):

        if d == 0:
            return 0

        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]

        for i in range(1, target + 1):
            dp[0][i] = 0
        for j in range(1, d + 1):
            dp[j][0] = 0

        dp[0][0] = 1

        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]

        return dp[d][target] % ((10 ** 9) + 7)


#         def recursive(d, f, target):

#             if target == 0 and d == 0:
#                 return 1

#             if target < 0 or d == 0:
#                 return 0

#             if dp[d][target] != -1:
#                 return dp[d][target]
#             temp = 0
#             for i in range(1, f+1):
#                 temp += recursive(d - 1, f, target - i)

#             dp[d][target] =  temp
#             return dp[d][target]

#         return (recursive(d, f, target) % ((10 ** 9) + 7))
