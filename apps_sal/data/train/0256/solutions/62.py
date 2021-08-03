class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        from math import ceil
        left = 1
        right = max(piles) + 1
        def timeConsumption(speed): return sum(ceil(pile / speed) for pile in piles)
        while left < right:
            mid = left + (right - left) // 2
            time = timeConsumption(mid)
            if time > H:
                left = mid + 1
            else:
                right = mid
        return left
