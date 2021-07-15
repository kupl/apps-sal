class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(maxsize=None)
        def helper(amount):
            if amount <= 0:
                return 0
            min_so_far = math.inf
            for i in range(len(coins)):
                if coins[i] <= amount:
                    min_so_far = min(min_so_far, 1 + helper(amount - coins[i]))
            return min_so_far

        result = helper(amount)
        if result == math.inf:
            return -1
        return result
