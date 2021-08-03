class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        lo, hi = max(weights), sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2
            tot, res = 0, 1
            for a in weights:
                if a + tot > mid:
                    tot = a
                    res += 1
                else:
                    tot += a
            if res <= D:
                hi = mid
            else:
                lo = mid + 1
        return lo
