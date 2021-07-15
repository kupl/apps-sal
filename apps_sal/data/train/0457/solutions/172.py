class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = {}
        res[0] = 0
        
        for x in range(amount+1)[1:]:
            prevs = [x-c for c in coins]
            
            
            
            this_res = min([res.get(y,2**31) for y in prevs])+1
            
            res[x] = this_res
        # print(res)
        if res[amount] >= 2**31:
            return -1
        else:
            return res[amount]
                    
            

