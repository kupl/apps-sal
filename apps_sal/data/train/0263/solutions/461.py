class Solution:
    def knightDialer(self, n: int) -> int:

        dp = [1] * 10
        if n == 1:
            return 10
        for i in range(n - 1):
            dpc = dp[:]
            dpc[0] = dp[4] + dp[6]
            dpc[1] = dp[6] + dp[8]
            dpc[2] = dp[7] + dp[9]
            dpc[3] = dp[4] + dp[8]
            dpc[4] = dp[9] + dp[3] + dp[0]
            dpc[5] = 0
            dpc[6] = dp[7] + dp[1] + dp[0]
            dpc[7] = dp[6] + dp[2]
            dpc[8] = dp[1] + dp[3]
            dpc[9] = dp[2] + dp[4]
            dp = dpc
        return sum(dp) % (10**9 + 7)
