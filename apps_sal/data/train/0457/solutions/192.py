class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helpCoins(coins, amount, cache):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            
            if amount in cache:
                return cache[amount]
               
            curr_min = 999
            for coin in coins:
                to_go = helpCoins(coins, amount - coin, cache)
                if to_go >= 0 and to_go < curr_min:
                    curr_min = to_go + 1
            
            if curr_min == 999:
                cache[amount] = -1
            else:
                cache[amount] = curr_min
            
            return cache[amount]
        
        return helpCoins(coins, amount, {})
                

