class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def canEatAllBananas(speed):
            count = 0
            for pile in piles:
                if pile >= speed:
                    count += pile // speed
                if pile % speed != 0:
                    count += 1
            return count <= H
        low = 1
        high = max(piles)
        while low <= high:
            mid = low + (high - low) // 2
            if canEatAllBananas(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
