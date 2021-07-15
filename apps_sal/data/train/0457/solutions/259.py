# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         min_coins = float('inf')
#         def backtrack(tot, count):
#             nonlocal min_coins
#             if tot == 0:
#                 min_coins = min(min_coins, count)
#                 return
#             for coin in coins:
#                 if coin <= tot:
#                     backtrack(tot - coin, count + 1)
#         backtrack(amount, 0)
#         return -1 if min_coins == float('inf') else min_coins
    
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def backtrack(tot):            
            if tot == 0:
                return 0   
            if tot not in memo:
                min_coins = float('inf')
                for coin in coins:
                    if coin <= tot:
                        cur_count = backtrack(tot - coin) + 1
                        min_coins = min(min_coins, cur_count)
                memo[tot] = min_coins
            return memo[tot]
        out = backtrack(amount)
        return -1 if out == float('inf') else out

