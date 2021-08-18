class Solution:
    def countOrders(self, n: int) -> int:
        dp = {}
        dp[1] = 1

        for i in range(2, n + 1):
            num_digit, res = 2 * (i - 1), 0
            for j in range(num_digit + 1, 0, -1):
                res += j
            dp[i] = res * dp[i - 1]

        return dp[n] % (10**9 + 7)
