class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        #@functools.lru_cache(None)
        def helper(start):
            if len(s[start:]) == 0: return 0
            res = -math.inf
            for i in range(start+1,len(s)+1):
                if s[start:i] not in seen:
                    seen.add(s[start:i])
                    #print('seen',seen)
                    followup = helper(i)
                    res= max(res,1+followup)
                    #print('results',results,followup,len(seen),seen)
                    seen.remove(s[start:i])
            
            return res
        
        seen = set()
        return helper(0)
        

