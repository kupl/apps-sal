class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def finishable(piles, H, eatRate) -> bool:
            numHours = 0
            for pile in piles:
                numHours += ceil(pile / eatRate)

            return numHours <= H

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2

            if finishable(piles, H, mid):
                right = mid
            else:
                left = mid + 1

        return left
