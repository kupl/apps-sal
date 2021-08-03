from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)

        def banana_test(bans):
            return sum([ceil(pile / bans) for pile in piles]) <= H
        while left < right:
            mid = left + (right - left) // 2
            if banana_test(mid):
                right = mid
            else:
                left = mid + 1
        return left
