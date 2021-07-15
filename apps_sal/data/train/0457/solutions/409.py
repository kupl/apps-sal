from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dict_ = set(coins)
        count = [0]*amount
        # Top down approach
        def top_down(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if count[rem - 1] != 0: # cache
                return count[rem - 1];
            
            min_ = float('inf')
            
            for coin in dict_:
                res = top_down(rem - coin)
                if res >= 0:
                    min_ = min(1 + res, min_)
            
            count[rem - 1] = -1 if min_ == float('inf') else min_
            return count[rem - 1]
        
    
        # bottom up approach
        def bottom_up():
            dpa = [float('inf')] * (amount + 1)
            dpa[0] = 0

            for i in range(1, len(dpa)):
                for coin in dict_:
                    if i >= coin:
                        remainder = i - coin
                        dpa[i] = min(dpa[remainder] + 1, dpa[i])
            return dpa[amount] if dpa[amount] != float('inf') else -1 
        
        
        return bottom_up()
        # return top_down(amount)    
        

    
    
        
        
        
                
            
            

