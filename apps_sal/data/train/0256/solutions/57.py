import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        start, end = 1, max(piles)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_feasible(piles, H, mid) == False:
                start = mid + 1
            elif self.is_feasible(piles, H, mid) == True:
                end = mid
        if self.is_feasible(piles, H, start):
            return start
        else:
            return end

    def is_feasible(self, piles, H, speed):
        res = 0
        for i in piles:
            res += math.ceil(i / speed)
        if res <= H:
            return True
        else:
            return False
