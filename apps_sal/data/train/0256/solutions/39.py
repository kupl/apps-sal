class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo = 1
        hi = max(piles)
        
        while lo < hi:
            mid = (hi - lo) // 2 + lo
            if sum([math.ceil(i/mid) for i in piles]) > H:
                lo = mid + 1
            else:
                hi = mid
        return lo

