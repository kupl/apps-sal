class Solution:

    def countOrders(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n + 1):
            res = dp[i - 1] * (2 * (i - 1) + 1) * (2 * (i - 1) + 2) // 2
            res = res % (10 ** 9 + 7)
            dp.append(res)
        return dp[n]
