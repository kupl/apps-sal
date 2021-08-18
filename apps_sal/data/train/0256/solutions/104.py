class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        lo = max(1, sum(piles) // H)
        hi = max(piles)

        while lo < hi:

            mid = (lo + hi) // 2

            t_lo = self.time_taken(piles, lo)
            t_mid = self.time_taken(piles, mid)

            if t_lo <= H:
                return lo
            elif t_mid <= H:
                hi = mid
                lo += 1
            else:
                lo = mid + 1

        return lo

    def time_taken(self, piles, n):

        return sum(v // n + (1 if v % n else 0) for v in piles)
