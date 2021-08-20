class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        def helper(amount, minAmounts):
            if amount == 0:
                return 0
            elif amount < 0:
                return math.inf
            if amount in minAmounts:
                return minAmounts[amount]
            minAmount = math.inf
            for coin in coins:
                minAmount = min(minAmount, helper(amount - coin, minAmounts) + 1)
            minAmounts[amount] = minAmount
            return minAmount
        minAmounts = dict()
        x = helper(amount, minAmounts)
        if x == math.inf:
            return -1
        return x
