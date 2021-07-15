class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo, hi = 1, max(piles)
        while lo <= hi:
            k = lo + (hi - lo) // 2
            if self.finish(k, piles) <= H: # count time to eat all bananas at speed K
                hi = k - 1
            else:
                lo = k + 1
        return lo
    
    def finish(self, k, piles):
        res = 0
        for pile in piles:
            res += pile // k
            if pile % k != 0:
                res += 1
        return res

