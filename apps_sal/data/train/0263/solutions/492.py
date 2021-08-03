class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        mod = 10**9 + 7
        for i in range(1, n):
            dp_old = dp.copy()
            dp[0] = dp_old[4] + dp_old[6]
            dp[1] = dp_old[6] + dp_old[8]
            dp[2] = dp_old[7] + dp_old[9]
            dp[3] = dp_old[4] + dp_old[8]
            dp[4] = dp_old[3] + dp_old[9] + dp_old[0]
            dp[5] = 0
            dp[6] = dp_old[1] + dp_old[7] + dp_old[0]
            dp[7] = dp_old[2] + dp_old[6]
            dp[8] = dp_old[1] + dp_old[3]
            dp[9] = dp_old[2] + dp_old[4]

        return sum(dp) % mod
