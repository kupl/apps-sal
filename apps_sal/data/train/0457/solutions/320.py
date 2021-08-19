class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinChangeHelper(coins, amount, memoisation={}):
            # memoisation hashmap - key (the amount), value(the minimum coins)

            if amount == 0:  # Base case 1
                return 0

            if amount < 0:  # Base case 2: This combination of coins was not successfull
                return float('inf')

            if amount in memoisation:  # If we have already computed the minimum for this amount before, return cached value
                return memoisation[amount]

            min_coins_used = float('inf')  # Keep track of the minimum coins used
            for i in range(len(coins) - 1, -1, -1):  # If the amount is not cached, consider all the coin denominations
                min_coins_used = min(1 + coinChangeHelper(coins, amount - coins[i], memoisation), min_coins_used)

            memoisation[amount] = min_coins_used
            return min_coins_used

        result = coinChangeHelper(coins, amount)
        return result if result != float('inf') else -1


#         def helper(coins, amount):
#             if amount == 0:
#                 return 1
#             if amount < 0:
#                 return float('inf')

#             min_so_far = float('inf')
#             for denomination in reversed(coins):
#                 min_so_far = min(min_so_far, helper(coins, amount - denomination))

#             return min_so_far + 1 if min_so_far != float('inf') else -1

#         result = helper(coins, amount)
#         return  result - 1 if result > 0 else -1
