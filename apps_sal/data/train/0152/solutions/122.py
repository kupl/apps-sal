class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo, hi = 1, position[-1] - position[0]
        while lo < hi:
            mi, t, y = (lo + hi + 1) // 2, 1, position[0]
            for x in position:
                if x - y >= mi:
                    y, t = x, t + 1
            if t < m:
                hi = mi - 1
            else:
                lo = mi
        return lo
