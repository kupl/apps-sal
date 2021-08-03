class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left2right = [0] * len(prices)
        right2left = [0] * len(prices)
        dp = prices[:]

        max_profit = 0
        for i in range(1, len(prices)):
            dp[i] = min(dp[i - 1], prices[i])
            left2right[i] = max(left2right[i], prices[i] - dp[i])
            max_profit = max(max_profit, prices[i] - dp[i])

        dp = prices[:]
        for i in reversed(list(range(len(prices) - 1))):
            dp[i] = max(dp[i + 1], prices[i])
            right2left[i] = max(right2left[i + 1], dp[i] - prices[i])

        print(right2left)

        for i in range(len(prices) - 1):
            max_profit = max(max_profit, left2right[i] + right2left[i + 1])

        return max_profit
