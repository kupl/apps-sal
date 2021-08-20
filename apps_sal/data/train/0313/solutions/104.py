class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def possible(days):
            bonquets = flowers = 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m
        if len(bloomDay) < m * k:
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + right >> 1
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left if possible(left) else -1
