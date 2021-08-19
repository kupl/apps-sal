class Solution:

    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        else:
            dp = [0 for _ in range(n + 1)]
            dp[n] = 1 / n
            for i in range(n - 1, 1, -1):
                dp[i] = dp[i + 1] / i + dp[i + 1]
            return dp[2]
