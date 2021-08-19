class Solution:

    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        if n == 2:
            return 0.5
        dp = [0] * n
        dp[0] = 1 / n
        for i in range(1, n - 1):
            dp[i] = 0.5 / n
        return sum(dp)
