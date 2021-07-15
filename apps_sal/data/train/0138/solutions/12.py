class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxlen = 0
        curlen = 0
        tmplen = 0
        even = True 
        for i in nums:
            if i == 0:
                if tmplen != curlen:
                    # We meet odd numbers of negative number, check if the rest is larger
                    maxlen = max(maxlen, tmplen - curlen - 1)
                maxlen = max(maxlen, curlen)
                curlen = 0
                tmplen = 0
                even = True
                continue
            tmplen += 1    
            if i < 0:    
                even = not even
                if even == True:
                    curlen = tmplen        
            if i > 0 and even == True:
                curlen += 1      
        if tmplen != curlen:
            # We meet odd numbers of negative number, check if the rest is larger
            maxlen = max(maxlen, tmplen - curlen - 1)
        maxlen = max(maxlen, curlen)        
        
        curlen = 0
        tmplen = 0
        even = True 
        for i in reversed(nums):
            if i == 0:
                if tmplen != curlen:
                    # We meet odd numbers of negative number, check if the rest is larger
                    maxlen = max(maxlen, tmplen - curlen - 1)
                maxlen = max(maxlen, curlen)
                curlen = 0
                tmplen = 0
                even = True
                continue
            tmplen += 1    
            if i < 0:    
                even = not even
                if even == True:
                    curlen = tmplen        
            if i > 0 and even == True:
                curlen += 1      
        if tmplen != curlen:
            # We meet odd numbers of negative number, check if the rest is larger
            maxlen = max(maxlen, tmplen - curlen - 1)
        maxlen = max(maxlen, curlen)        
        
        return maxlen       

