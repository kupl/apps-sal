class Solution:
    def coinChange(self, coins, amount):
        coins.sort(reverse=True)
        lenc, self.res = len(coins), 2**31 - 1

        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res - count):  # if hope still exists
                    dfs(i, rem - coins[i], count + 1)

        for i in range(lenc):
            dfs(i, amount, 0)
        return self.res if self.res < 2**31 - 1 else -1

#       def coinChange(self, coins: List[int], amount: int) -> int:
#         coins.sort(reverse = True)
#         min_coins = float('inf')

#         def count_coins(start_coin, coin_count, remaining_amount):
#             nonlocal min_coins

#             if remaining_amount == 0:
#             min_coins = min(min_coins, coin_count)
#             return

#           # Iterate from largest coins to smallest coins
#             for i in range(start_coin, len(coins)):
#             remaining_coin_allowance = min_coins - coin_count
#             max_amount_possible = coins[i] * remaining_coin_allowance

#             if coins[i] <= remaining_amount and remaining_amount < max_amount_possible:
#                 count_coins(i, coin_count + 1, remaining_amount - coins[i])

#         count_coins(0, 0, amount)
#         return min_coins if min_coins < float('inf') else -1
