class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        minK = 1
        maxK = 0
        for pile in piles:
            if pile > maxK:
                maxK = pile

        low = minK
        high = maxK
        mid = (low + high) // 2

        while (low < high):
            testK = mid
            if (self.validK(piles, H, mid)):
                high = mid
            else:
                low = mid + 1

            mid = (low + high) // 2
        return high

    def validK(self, piles, H, eatspeed):
        hourCount = 0
        for pile in piles:
            hoursUsed = ceil(pile / eatspeed)
            hourCount += hoursUsed
            if hourCount > H:
                return False

        return True
