class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay): return -1
        
        M = max(bloomDay)
        lo, hi= 0,M
        
        def works(h):
            curr = 0
            bou = 0
            for b in bloomDay:
                if b<=h:
                    curr+=1
                    if curr==k:
                        bou+=1
                        curr=0
                    if bou==m:
                        return True
                else:
                    curr=0
        
        while hi-lo>1:
            h = (hi+lo)//2
            if works(h):
                hi=h
            else:
                lo=h
        
        return hi     
