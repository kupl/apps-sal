class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def can_eat(x: int, h: int) -> bool:
            hrs = 0
            for p in piles:
                if p <= x:
                    hrs += 1
                else:
                    hrs += p // x + 1
                if hrs > h:
                    return False
            return True
        (low, high) = (1, max(piles))
        while low < high:
            mid = low + (high - low) // 2
            if can_eat(mid, H):
                high = mid
            else:
                low = mid + 1
        return low
