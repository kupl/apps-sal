class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def recurse(amount,pos):
            if pos==len(coins):
                return 10000
            if amount ==0:
                return 0
            
            
            if coins[pos]<=amount:
                return min(recurse(amount-coins[pos],pos)+1,
                          recurse(amount,pos+1))
            else:
                return recurse(amount,pos+1)
            
            
        count = recurse(amount,0)
        if count>=10000:
            return -1
        return count
            
            

