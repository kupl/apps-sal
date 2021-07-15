class Solution:
# min(cnt(11-1),cnt(11-2),cnt(11-5))     
    def coinChange(self, coins: List[int], total: int) -> int:
        dic = {0:0,}
        
        def helper(amount):
            
            if amount in coins:
                dic[amount] = 1
            
            elif amount<0:
                return float('inf')
            
            elif amount not in dic:
                dic[amount] = min([helper(amount-c)+1 for c in coins])
            
            return dic[amount]
        
        return helper(total) if helper(total)!=float('inf') else -1

