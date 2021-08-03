class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        # 0 for buy 1 for sell 2 for break
        dp = [[-9999999] * len(prices) for _ in range(3)]
        dp[0][0], dp[1][0], dp[2][0] = -prices[0], 0, 0
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i - 1], dp[2][i - 1] - prices[i])
            dp[1][i] = max(dp[0][i - 1] + prices[i], dp[1][i - 1])
            dp[2][i] = max(dp[2][i - 1], dp[0][i - 1], dp[1][i - 1])
        return max(dp[1][-1], dp[2][-1])
