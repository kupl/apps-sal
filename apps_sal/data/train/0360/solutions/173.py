class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def can(x):
            res, sum = 1, 0
            for w in weights:
                if w > x:
                    return False
                if sum + w > x:
                    res += 1
                    sum = w
                else:
                    sum += w
            return res <= D
        mx, sum = 0, 0
        for i in weights:
            mx, sum = max(mx, i), sum + i
        lo, hi = mx, sum
        while lo < hi:
            mi = (hi - lo) // 2 + lo
            if not can(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
