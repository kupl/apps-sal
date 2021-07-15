class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def feasible(bananas):
            hour = 0
            for pile in piles:
                hs, left = divmod(pile, bananas)
                hour += hs + (left > 0)
            return hour <= H
            
        l = 1
        r = sum(piles)
            
        while l < r:
            mid = (l+r)>>1
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
