class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo = sum(piles) // H

        hi = max(piles)

        if len(piles) == 1:
            return ceil(piles[0] / H)

        while lo <= hi:
            mid = (lo + hi) // 2

            count = sum(map(lambda x: ceil(x / mid), piles))

            if count > H:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo
