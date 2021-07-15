import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        end = max(piles)
        start = 1
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if self.possible(mid, piles, H):
                end = mid 
            else:
                start = mid 
        
        if self.possible(start,piles,H):
            return start 
        if self.possible(end, piles, H):
            return end 
        
    
    def possible(self, eat_load, total_load, hour):
        return sum([math.ceil(-k / -eat_load) for k in total_load]) <= hour 
