class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low = 1
        high = max(piles)

        def possible(k):
            time = 0
            for pile in piles:
                time += (pile - 1) // k + 1
            return time <= H
        while low <= high:
            mid = low + (high - low) // 2
            outcome = possible(mid)
            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
