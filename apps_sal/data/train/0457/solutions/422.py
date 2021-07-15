class Solution:
    def aux(self, coins, amount, cache):
        if amount in cache: 
            return cache[amount]

        
        res = -1
        for i in range(len(coins)):
            if coins[i] < amount:
                right = cache[amount-coins[i]] if amount-coins[i] in cache else self.aux(coins, amount-coins[i], cache)
                
                if right!=-1 and res==-1:
                    res = 1+right
                elif right!=-1 and res!=-1:
                    res = min(res, 1+right)
                    
                
        
        cache[amount] = res
        return cache[amount]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0: return 0
        cache = dict(list(zip(coins, [1]*len(coins))))
        return self.aux(coins, amount, cache)
        
        
        
        

