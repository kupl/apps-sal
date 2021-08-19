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
    "def helper(self, coins, amount, dp):\n        if amount < 0:\n            return float('inf')\n        if amount == 0:\n            return 0\n        if amount in dp:\n            return dp[amount]\n        for i in range(len(coins)):\n            use_ci = 1 + self.helper(coins, amount - coins[i], dp)\n            if amount not in dp:\n                dp[amount] = use_ci\n            else:\n                dp[amount] = min(dp[amount], use_ci)       \n        return dp[amount]\n       \n    def coinChange(self, coins: List[int], amount: int) -> int:\n        if amount <= 0:\n            return 0\n        dp = {}\n        result = self.helper(coins, amount, dp)\n        return -1 if result == float('inf') else result"
