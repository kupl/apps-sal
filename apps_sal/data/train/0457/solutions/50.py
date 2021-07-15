class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        arr = [float('inf')] * (amount+1) 
        arr[0] = 0
        
        for i in range(amount+1):
            for c in coins:
                if i+c > amount:
                    continue
                                
                if arr[i+c] > arr[i] + 1:
                    arr[i+c] = arr[i] + 1
                    
        
        if arr[-1] == float('inf'):
            return -1
        
        return arr[-1]
                    

