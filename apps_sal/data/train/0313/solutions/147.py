class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def feasible(days) -> bool:
            (bouquets, flowers) = (0, 0)
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bouquets >= m
        if len(bloomDay) < m * k:
            return -1
        (left, right) = (1, max(bloomDay))
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
