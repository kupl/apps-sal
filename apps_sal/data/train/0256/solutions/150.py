class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if self.__getEatHours(piles, mid) <= H:
                right = mid
            else:
                left = mid + 1
        return left

    def __getEatHours(self, piles, speed):
        hours = 0
        for p in piles:
            hours += p // speed
            if p % speed != 0:
                hours += 1
        return hours
