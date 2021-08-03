class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        #         max_position = max(steps, arrLen)
        #         dp = [[0] * (max_position + 1) for step in range(steps+1)]

        #         dp[1][0] = 1
        #         dp[1][1] = 1

        #         for i in range(2, steps + 1):
        #             for j in range(0, max_position):
        #                 if j > 0:
        #                     dp[i][j] = (dp[i-1][j] + dp[i-1][j+1] + dp[i-1][j-1]) % (10 ** 9 + 7)
        #                 else:
        #                     dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % (10 ** 9 + 7)

        #         return dp[steps][0]

        mod = 10 ** 9 + 7
        n = arrLen

        A = [0, 1]
        for t in range(steps):
            A[1:] = [sum(A[i - 1:i + 2]) % mod for i in range(1, min(n + 1, t + 3))]

        return A[1] % mod
#         ways = [-1, 0, 1]

#         def visit(cur_total_steps, cur_index):
#             if cur_total_steps == steps and cur_index == 0:
#                 self.total_ways += 1
#                 return

#             if cur_total_steps > steps or cur_index >= arrLen:
#                 return

#             for way in ways:
#                 if cur_index == 0 and way == -1:
#                     continue

#                 if cur_index == arrLen - 1 and way == 1:
#                     continue

#                 visit(cur_total_steps + 1, cur_index + way)

#         self.total_ways = 0
#         visit(0, 0)

#         return self.total_ways % (10^9 + 7)
