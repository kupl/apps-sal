class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        N = len(hats)
        ppl = dict()
        for i, hat in enumerate(hats):
            for x in hat:
                ppl.setdefault(x, []).append(i)
                
        @lru_cache(None)
        def helper(h, mask):
            
            if mask == (1 << N) - 1: return 1  ## if mask covered all the people set bits == people
            if h == 40: return 0 ## if all hats are being used
            
            ans = helper(h+1, mask)
            
            for p in ppl.get(h+1, []): ## loop through all the people preferring the hat
                if mask & (1 << p):  ## if taken already continue
                    continue
                    
                mask |= 1 << p  ## set bit
                
                ans += helper(h+1, mask)
                
                mask ^= 1 << p  ## reset bit
                
            return ans% 1_000_000_007
        
        return helper(0, 0)

