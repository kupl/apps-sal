class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #let arr[i] be the min amt of coins needed to produce amount i
        arr = [float('inf')] * (amount+1)
        arr[0] = 0 
        
        for i in range(1, len(arr)): 
            min_choices = []
            for x in coins: 
                if i - x >= 0: 
                    min_choices.append(1 + arr[i-x])
            
            if min_choices: 
                arr[i] = min(min_choices)
        
        if arr[amount] == float('inf'): 
            return -1
        else: 
            return arr[amount]

