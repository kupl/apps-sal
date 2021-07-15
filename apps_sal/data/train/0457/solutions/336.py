class Solution:
    memory = {}
    
    
    def numCoins(self, coins, amount):
        if amount in self.memory:
            return self.memory[amount]
        
        if amount == 0:
            return 0
        
        ncarr = []
        carr = []
        for c in coins:
            if amount >= c:
                nnc = self.numCoins(coins, amount - c)                
                ncarr.append(nnc + 1)
                carr.append(c)
            
        if len(ncarr) > 0:        
            nc = min(ncarr)
            #accum += carr[ncarr.index(nc)]
            self.memory[amount] = nc
            return nc
        else:
            return float('inf')
    
                        
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memory = {}                
        nc = self.numCoins(coins, amount)
        if nc == float('inf'):
            return -1
        
        return nc
        
            
        
        

