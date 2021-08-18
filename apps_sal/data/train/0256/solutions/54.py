import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def isValid(mid):
            hours = 0
            for banana in piles:

                div = math.ceil(banana / mid)
                hours += div
                if hours > H:
                    return False
            return True

        def binsearch():
            low = 1
            high = sum(piles)
            while low < high:
                mid = low + (high - low) // 2
                if isValid(mid):
                    high = mid
                else:
                    low = mid + 1
            return low
        total = sum(piles)
        return binsearch()
