import bisect


class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        pos = sorted(position)
        if m == 2:
            return pos[-1] - pos[0]

        def isFeasible(d):
            j = 0
            for k in range(1, m):
                j = bisect.bisect_left(pos, pos[j] + d, j + 1)
                if j == n:
                    return False
            return True
        res = -1
        (lo, hi) = (1, pos[-1] - pos[0] + 1)
        while lo < hi:
            d = (lo + hi) // 2
            print(lo, hi, d)
            if isFeasible(d):
                lo = d + 1
            else:
                hi = d
        return hi - 1
