class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if self.condition(piles, H, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def condition(self, piles, H, k):
        hours = 0
        for pile in piles:
            div, rem = divmod(pile, k)
            hours += div
            if rem != 0:
                hours += 1
        return hours <= H
