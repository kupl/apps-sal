import math

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(K):
            return sum(math.ceil(p/K) for p in piles) <= H
        
        low = 1
        high = max(piles) + 1
        
        while low < high:
            mid = low + ((high - low) // 2)
            if possible(mid):
                high = mid
            else:
                low = mid + 1
                
        return low
