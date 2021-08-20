class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def possible(K):
            return sum((math.ceil(p / K) for p in piles)) <= H
        (lo, hi) = (1, max(piles))
        while lo < hi:
            mid = int(lo + (hi - lo) / 2)
            if not possible(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
