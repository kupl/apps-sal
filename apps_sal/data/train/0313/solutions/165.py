class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def feasible(days: int):
            (flowers, bouquets) = (0, 0)
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bouquets >= m
        if len(bloomDay) < m * k:
            return -1
        (low, high) = (1, max(bloomDay))
        while low < high:
            mid = low + (high - low) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
