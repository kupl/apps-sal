class Solution:   
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        self.count = [float('inf')]*(amount + 1)
        self.count[0] = 0
        # print(count)
        
        for i in range(1, amount + 1):
            for coin in coins:
                rest = i - coin
                if rest >= 0 and self.count[rest] != float('inf'):
                    self.count[i] = min(1 + self.count[rest], self.count[i])
                    
        if self.count[-1] == float('inf'): 
            return -1
        else:
            return self.count[-1]
    

                
                

