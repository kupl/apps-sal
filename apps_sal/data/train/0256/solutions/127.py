class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def can_finish(piles, K, H):
            return sum([(p + K - 1) // K for p in piles]) <= H
        low = 1
        high = max(piles)
        while low < high:
            mid = low + (high - low) // 2
            if can_finish(piles, mid, H):
                high = mid
            else:
                low = mid + 1
        return low
