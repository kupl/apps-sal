class Solution:
    def minDays(self, n: int) -> int:
        dp = {}
        dp[0] = 1

        def getMinDays(n, dp):
            if n == 0:
                return 0
            if n - 1 in dp:
                return dp[n - 1]
            eat2 = n % 2 + getMinDays(n // 2, dp) + 1
            eat3 = n % 3 + getMinDays(n // 3, dp) + 1
            dp[n - 1] = min(eat2, eat3)
            return dp[n - 1]
        return getMinDays(n, dp)
