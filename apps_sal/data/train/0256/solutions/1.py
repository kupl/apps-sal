import math


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        total_bananas = sum(piles)
        (left, right) = (math.ceil(total_bananas / H), math.ceil(total_bananas / (H - len(piles) + 1)))
        while left < right:
            mid = (left + right) // 2
            if not sum([math.ceil(pile / mid) for pile in piles]) <= H:
                left = mid + 1
            else:
                right = mid
        return left
