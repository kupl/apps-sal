class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def feasible(days):
            (bouquets, flowers) = (0, 0)
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bouquets >= m
        if m * k > len(bloomDay):
            return -1
        (lo, hi) = (1, max(bloomDay))
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
