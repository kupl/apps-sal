class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxl = 0
        
        posi = None
        start = -1
        cur = True
        for i,n in enumerate(nums):
            if n == 0:
                start = i
                posi = None
                cur = True
                
            elif n > 0:
                if cur:
                    maxl = max(maxl,i-start)
                    
                else:
                    if posi == None:
                        maxl = max(maxl,1)
                        posi = i
                    else:
                        maxl = max(maxl,i-posi+1)
                 
                
            else:
                if not cur:
                    maxl = max(maxl,i-start)
                    if not posi:
                        posi = i
                    cur = True
                else:
                    cur = False
                     
                    if posi:                        
                        maxl = max(maxl,i-posi+1)
                 
        return maxl
