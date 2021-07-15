class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 1 and coins[0] > amount:
            return -1
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        return dp[amount] if dp[amount] != amount+1 else -1
    
#         rs = [amount+1] * (amount+1)
#         rs[0] = 0
#         for i in xrange(1, amount+1):
#             for c in coins:
#                 if i >= c:
#                     rs[i] = min(rs[i], rs[i-c] + 1)

#         if rs[amount] == amount+1:
#             return -1
#         return rs[amount]

