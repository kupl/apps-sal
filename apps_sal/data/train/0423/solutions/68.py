class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        
        if not arr:return 0
        maxlen=1
        helper={}
        
        for i,x in enumerate(arr):
            
            if x-d in helper:
                helper[x]=helper[x-d]+1
                
            else:
                helper[x]=1
                
            maxlen=max(maxlen,helper[x])
            
            
        return maxlen
            
        

