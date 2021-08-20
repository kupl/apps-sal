class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        valid_status = [0, [prices[0], -prices[0]], 0]
        for t in range(1, len(prices)):
            valid_status[1][0] = prices[t]
            cool_down_temp = sum(valid_status[1])
            if valid_status[0] > sum(valid_status[1]):
                valid_status[1] = [prices[t], valid_status[0] - prices[t]]
            if valid_status[2] > valid_status[0]:
                valid_status[0] = valid_status[2]
            valid_status[2] = cool_down_temp
        return max(valid_status[0], valid_status[2])
