class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def time_used(T):
            return sum((p // T + (1 if p % T else 0) for p in piles))
        low = max(sum(piles) // H, 1)
        if time_used(low) <= H:
            return low
        high = max(piles)
        while low + 1 < high:
            mid = (low + high) // 2
            if time_used(mid) > H:
                low = mid
            else:
                high = mid
        return high
