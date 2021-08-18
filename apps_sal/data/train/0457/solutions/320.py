class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinChangeHelper(coins, amount, memoisation={}):

            if amount == 0:
                return 0

            if amount < 0:
                return float('inf')

            if amount in memoisation:
                return memoisation[amount]

            min_coins_used = float('inf')
            for i in range(len(coins) - 1, -1, -1):
                min_coins_used = min(1 + coinChangeHelper(coins, amount - coins[i], memoisation), min_coins_used)

            memoisation[amount] = min_coins_used
            return min_coins_used

        result = coinChangeHelper(coins, amount)
        return result if result != float('inf') else -1
