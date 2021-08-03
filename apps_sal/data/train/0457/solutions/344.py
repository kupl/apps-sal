import sys


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        res = self.helper(sorted(coins, reverse=True), amount, {})
        if res == float('inf'):
            return -1
        return res

    def helper(self, coins, amount, dAmounts):
        if amount < 0:
            return float('inf')

        if amount == 0:
            return 0

        if amount in dAmounts:
            return dAmounts[amount]

        for c in coins:
            pathCount = 1 + self.helper(coins, amount - c, dAmounts)
            dAmounts[amount] = min(dAmounts.get(amount, pathCount), pathCount)
        return dAmounts[amount]

    '''def helper(self, coins, amount, dp):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        if amount in dp:
            return dp[amount]
        for i in range(len(coins)):
            use_ci = 1 + self.helper(coins, amount - coins[i], dp)
            if amount not in dp:
                dp[amount] = use_ci
            else:
                dp[amount] = min(dp[amount], use_ci)       
        return dp[amount]
       
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        dp = {}
        result = self.helper(coins, amount, dp)
        return -1 if result == float('inf') else result'''
