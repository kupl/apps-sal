import math


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        """
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            return sum((p-1) / K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
        """
        le = 1
        ri = sum(piles)

        def checkHours(speed):
            s = 0
            for item in piles:
                s += math.ceil(item / speed)
            return s
            '\n            sum_hours = 0\n            for i in piles:\n                bananas =  i\n                hours = 0\n                while True:\n                    bananas = bananas - speed\n                    hours += 1\n                    if bananas <= 0: # bug only <\n                        break\n                sum_hours += hours\n            return sum_hours\n            '
        while le + 1 < ri:
            mid = le + (ri - le) // 2
            result = checkHours(mid)
            if result <= H:
                ri = mid
            else:
                le = mid
        result = checkHours(le)
        if result <= H:
            return le
        else:
            return ri
