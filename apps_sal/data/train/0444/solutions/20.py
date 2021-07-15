class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        if n == 2:
            return 0.5
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 0.5
        acc = 1.5
        for i in range(3, n + 1):
            dp[i] = (1.0 / i) * acc
            acc += dp[i]
        return dp[-1]
