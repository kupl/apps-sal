class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        dp = [0] * (n + 1)
        if n > 0:
            dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] / 2 + (1 - dp[i - 1]) / 2
        return dp[n]
