class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            if sum((pile // mid + (pile % mid > 0) for pile in piles)) > H:
                low = mid + 1
            else:
                high = mid
        return low
