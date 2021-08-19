class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def make_boquets(mid):
            (bonquets, flowers) = (0, 0)
            for bloom in bloomDay:
                if bloom > mid:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m
        (left, right) = (min(bloomDay), max(bloomDay) + 1)
        while left < right:
            mid = left + (right - left) // 2
            if make_boquets(mid):
                right = mid
            else:
                left = mid + 1
        if left > max(bloomDay):
            return -1
        return left
