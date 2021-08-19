import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        lo = int(math.ceil(sum(piles) / H))
        hi = sum(piles)
        # print(hi)

        def hours(j): return sum([int(math.ceil(i / j)) for i in piles])

        out = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            res = hours(mid)
            # print(res, mid)

            if res <= H:
                out = mid
            if res <= H:
                hi = mid - 1
            else:
                lo = mid + 1

        return out
