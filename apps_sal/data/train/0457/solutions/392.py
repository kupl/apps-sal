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
#         bottom-up DP
        memo = [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins))]
        for x in range(len(coins)):
            memo[x][0] = 0        
        for i, coin in enumerate(coins):            
            for tot in range(1, amount + 1):
                if i > 0: 
                    memo[i][tot] = memo[i - 1][tot]
                if coin <= tot:
                    memo[i][tot] = min(memo[i][tot], memo[i][tot - coin] + 1)
        out = memo[len(coins) - 1][amount]
        return -1 if out == float('inf') else out

        
#         top-down DP
        # memo = {}
        # def backtrack(tot):            
        #     if tot == 0:
        #         return 0   
        #     if tot not in memo:
        #         min_coins = float('inf')
        #         for coin in coins:
        #             if coin <= tot:
        #                 cur_count = backtrack(tot - coin) + 1
        #                 min_coins = min(min_coins, cur_count)
        #         memo[tot] = min_coins
        #     return memo[tot]
        # out = backtrack(amount)
        # return -1 if out == float('inf') else out

