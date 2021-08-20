class Solution:

    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        MOD = 10 ** 9 + 7
        for i in range(2, n + 1):
            old_dp = dp.copy()
            dp[0] = old_dp[4] + old_dp[6]
            dp[1] = old_dp[6] + old_dp[8]
            dp[2] = old_dp[7] + old_dp[9]
            dp[3] = old_dp[4] + old_dp[8]
            dp[4] = old_dp[3] + old_dp[9] + old_dp[0]
            dp[5] = 0
            dp[6] = old_dp[1] + old_dp[7] + old_dp[0]
            dp[7] = old_dp[2] + old_dp[6]
            dp[8] = old_dp[1] + old_dp[3]
            dp[9] = old_dp[2] + old_dp[4]
        ans = sum(dp) % MOD
        return ans
