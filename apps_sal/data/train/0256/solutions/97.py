class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def time_needed(piles, time):
            return sum(p//time + (1 if p%time else 0) for p in piles)
        
        lower = max(sum(piles)//H, 1)
        upper = max(piles)
        
        while lower < upper:
            time_lower = time_needed(piles, lower)
            if time_lower <= H:
                return lower
            
            mid = (lower+upper)//2
            time_mid = time_needed(piles, mid)
            if time_mid <= H:
                upper = mid
            else:
                lower = mid+1
                
        return lower
