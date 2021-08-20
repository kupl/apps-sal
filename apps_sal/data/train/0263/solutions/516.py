class Solution:

    def knightDialer(self, n: int) -> int:
        mexp = 10 ** 9 + 7
        dp = [1 for x in range(10)]
        for i in range(n - 1):
            ndp = [0 for x in range(10)]
            ndp[0] = (dp[4] + dp[6]) % mexp
            ndp[1] = (dp[6] + dp[8]) % mexp
            ndp[2] = (dp[7] + dp[9]) % mexp
            ndp[3] = (dp[4] + dp[8]) % mexp
            ndp[4] = (dp[0] + dp[3] + dp[9]) % mexp
            ndp[5] = 0
            ndp[6] = (dp[0] + dp[1] + dp[7]) % mexp
            ndp[7] = (dp[2] + dp[6]) % mexp
            ndp[8] = (dp[1] + dp[3]) % mexp
            ndp[9] = (dp[2] + dp[4]) % mexp
            dp = ndp
        return sum(dp) % mexp
