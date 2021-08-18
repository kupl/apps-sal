

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        coins = sorted(coins, reverse=True)

        def helper(coins, amount, cache):
            if amount == 0:
                return 0
            elif amount in cache:
                return cache[amount]
            cache[amount] = float('inf')
            for c in coins:
                if amount - c >= 0:
                    cache[amount] = min(cache[amount], helper(coins, amount - c, cache) + 1)
            return cache[amount]

        if amount == 0:
            return 0

        if min(coins) > amount:
            return -1

        ans = helper(coins, amount, {})

        return ans if ans != float('inf') else -1
