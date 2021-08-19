class Solution:

    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        elif n == 2:
            return 0.5
        dp = [0] * n
        dp[0] = 1
        dp[1] = 0.5
        sum1 = dp[1]
        for i in range(2, n):
            dp[i] = 1 / (i + 1) + 1 / (i + 1) * sum1
            sum1 += dp[i]
        return dp[-1]
