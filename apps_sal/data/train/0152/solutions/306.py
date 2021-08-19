class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (lo, hi) = (0, position[-1] - position[0])

        def check(amt):
            curr = position[0]
            cnt = 1
            for x in position[1:]:
                if x - curr >= amt:
                    cnt += 1
                    curr = x
            return cnt >= m
        while lo < hi:
            mi = (hi + lo + 1) // 2
            if check(mi):
                lo = mi
            else:
                hi = mi - 1
        return lo
