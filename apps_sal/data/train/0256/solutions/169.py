class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def feasible(threshold):
            count = 0
            for pile in piles:
                count += math.ceil(pile / threshold)
                if count > H:
                    return False
            return True
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left >> 1)
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
