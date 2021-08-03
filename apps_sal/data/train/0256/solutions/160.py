import math


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # 1 2 3 4 5 6 7 8 9 10 11

        def possible(x):
            if(x == 0):
                return False
            h = 0
            for i in piles:
                h += math.ceil(i / x)
            return h <= H

        high = max(piles)
        low = 1
        while(low < high):
            mid = low + (high - low) // 2
            if(possible(mid)):
                high = mid
            else:
                low = mid + 1
        return low
