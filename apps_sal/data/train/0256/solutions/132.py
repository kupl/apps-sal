class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        def eats(piles, h, k):
            hours = 0
            for pile in piles:
                hours += ((pile - 1) // k + 1)
            return hours <= h
        
        lo = 1
        hi = 10**9
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if eats(piles, H, mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo

