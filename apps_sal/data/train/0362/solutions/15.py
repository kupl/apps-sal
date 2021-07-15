class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        from collections import defaultdict
        from functools import lru_cache
        ppl=defaultdict(list)
        for i in range(len(hats)):
            for j in hats[i]:
                ppl[j].append(i)
                
                
        @lru_cache(None)
        def call(ht,mask):
            if mask==(1<<len(hats))-1:
                return 1
            if ht>40:
                return 0
            ans=call(ht+1,mask)
            for p in ppl[ht+1]:
                if mask&(1<<p):
                    continue
                mask|=(1<<p)
                ans+=call(ht+1,mask)
                mask^=(1<<p)
                
            return ans%(10**9 +7)
        return call(0,0)

