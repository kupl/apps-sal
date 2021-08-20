class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        # Notes:
            k adjacent flowers

        """
        n = len(bloomDay)
        if n // k < m:
            return -1
        if k * m == n:
            return max(bloomDay)

        def feasible(days) -> bool:
            (bonquets, flowers) = (0, 0)
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m
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
