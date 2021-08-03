class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = dict()

        def recursiveChange(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in cache:
                return cache[amount]

            min_val = float('inf')
            for coin_val in coins:
                combination = recursiveChange(amount - coin_val)
                if combination != -1:
                    min_val = min(min_val, combination + 1)
            cache[amount] = min_val
            return min_val

        ans = recursiveChange(amount)
        if ans == float('inf'):
            return -1
        return ans
