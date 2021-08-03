from math import ceil


def count_hr(piles, k):
    return sum([ceil(p / k) for p in piles])


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) > H:
            return
        lo, hi = 1, max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            if count_hr(piles, mid) > H:
                lo = mid + 1
            elif count_hr(piles, mid) <= H:
                hi = mid - 1

        return lo
