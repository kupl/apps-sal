class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1] * 10

        for _ in range(2, n + 1):
            dpc = dp.copy()
            dp[0] = dpc[4] + dpc[6]
            dp[1] = dpc[6] + dpc[8]
            dp[2] = dpc[7] + dpc[9]
            dp[3] = dpc[4] + dpc[8]
            dp[4] = dpc[3] + dpc[9] + dpc[0]
            dp[5] = 0
            dp[6] = dpc[1] + dpc[7] + dpc[0]
            dp[7] = dpc[2] + dpc[6]
            dp[8] = dpc[1] + dpc[3]
            dp[9] = dpc[4] + dpc[2]

        res = sum(dp) % mod
        return res
