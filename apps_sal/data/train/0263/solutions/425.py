class Solution:

    def knightDialer(self, n: int) -> int:
        dp = {i: 1 for i in range(10)}
        mod = 10 ** 9 + 7
        for _ in range(1, n):
            dp2 = {}
            dp2[0] = (dp[4] + dp[6]) % mod
            dp2[1] = (dp[6] + dp[8]) % mod
            dp2[2] = (dp[7] + dp[9]) % mod
            dp2[3] = (dp[4] + dp[8]) % mod
            dp2[4] = (dp[0] + dp[3] + dp[9]) % mod
            dp2[5] = 0
            dp2[6] = (dp[0] + dp[1] + dp[7]) % mod
            dp2[7] = (dp[2] + dp[6]) % mod
            dp2[8] = (dp[1] + dp[3]) % mod
            dp2[9] = (dp[2] + dp[4]) % mod
            dp = dp2
        return sum(dp.values()) % mod
