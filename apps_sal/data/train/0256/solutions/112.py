class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(K):
            return sum(ceil(pile / K) for pile in piles) <= H
        total = sum(piles)
        lo, hi = ceil(total / H), ceil(total / (H - len(piles) + 1))
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
