

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        # reverse the order
        coins = sorted(coins, reverse=True)

#         def recurse(amt, coins, currnumcoins):

#             if amt in cache:
#                 return cache[amt]

#             cache[amt] =  float('inf')
#             # base case
#             for coin in coins:
#                 if (amt - coin) == 0 :
#                     return currnumcoins + 1

#                 elif (amt - coin) > 0:
#                     cache[amt] =  min(recurse(amt-coin, coins, currnumcoins + 1), cache[amt])

#             return cache[amt]

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

        # ans = recurse(amount, coins, 0)
        ans = helper(coins, amount, {})

        return ans if ans != float('inf') else -1
