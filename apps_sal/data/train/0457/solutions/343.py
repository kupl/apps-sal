class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        seen = {0: 0}

        def helper(coins, amount):

            if amount in seen:
                return seen[amount]

            if not coins:
                return -1

            leastCoins = float('Inf')
            for coin in [c for c in coins if c <= amount]:
                next_least = helper(coins, amount - coin)
                if next_least != -1:
                    leastCoins = min(leastCoins, 1 + next_least)
            if leastCoins == float('Inf'):
                seen[amount] = -1
                return -1
            else:
                seen[amount] = leastCoins
                return leastCoins

        return helper(coins, amount)
