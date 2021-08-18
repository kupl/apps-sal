class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        n = len(weights)

        hi = 0
        lo = 0
        for w in weights:
            lo = max(lo, w)
            hi += w

        if D == 1:
            return hi

        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            cur, days = 0, 1
            for w in weights:
                cur += w
                if cur > mid:
                    days += 1
                    cur = w
            if days > D:
                lo = mid + 1
            else:
                hi = mid
        return lo
