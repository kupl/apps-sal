class Solution:
    def knightDialer(self, n: int) -> int:

        dp = [1 for x in range(10)]

        # jumpMap = {1: [6, 8], 2: [7, 9], 3: [8, 4], 4: [9, 3, 0]: 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [4, 2], 0: [4, 6]}

        for index in range(n - 1):

            newDp = [dp[4] + dp[6],
                     dp[6] + dp[8],
                     dp[7] + dp[9],
                     dp[8] + dp[4],
                     dp[9] + dp[3] + dp[0],
                     0,
                     dp[1] + dp[7] + dp[0],
                     dp[2] + dp[6],
                     dp[1] + dp[3],
                     dp[4] + dp[2]]

            dp = newDp

        return sum(dp) % (10**9 + 7)
