class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        N = len(piles)
        
        start = 1
        end = max(piles)
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if self._can_complete(piles, mid, H):
                end = mid
            else:
                start = mid
                
        if self._can_complete(piles, start, H):
            return start
        else:
            return end
        
    def _can_complete(self, piles, K, H):
        i = 0
        N = len(piles)
        
        c = 0
        for d in piles:
            c += math.ceil(d / K)
            
        return c <= H

