class Solution(object):

    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1
        if dp[amount] == MAX:
            return -1
        return dp[amount]
        return [dp[amount], -1][dp[amount] == MAX]
