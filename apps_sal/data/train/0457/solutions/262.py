class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        return self.painful(coins, amount, dp)

    def painful(self, coins: List[int], amount: int, dp: List[int]) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if dp[amount]:
            return dp[amount]
        minCost = math.inf
        for coin in coins:
            res = self.painful(coins, amount - coin, dp)
            if res != -1:
                minCost = min(minCost, 1 + res)
        dp[amount] = minCost if minCost < math.inf else -1
        return minCost if minCost < math.inf else -1
