class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def useDays(pile, speed):
            days = pile // speed
            return days if pile % speed == 0 else days + 1

        def CanDone(piles, speed, H):
            numDays = 0
            for num in piles:
                numDays += useDays(num, speed)
            return numDays <= H

        maxEat = max(piles)
        left, right = 1, maxEat + 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if CanDone(piles, mid, H):
                right = mid
            else:
                left = mid + 1
        return left
