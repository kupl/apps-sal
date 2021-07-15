class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        cache = {}
        
        def rec(amount):
            
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            val = float('inf')
            
            for coin in coins:
                
                if amount-coin >= 0:
                    val = min(val,1+rec(amount-coin))
            cache[amount] = val
            return val
            
        ans = rec(amount)
        return ans if ans != float('inf') else -1
                    

