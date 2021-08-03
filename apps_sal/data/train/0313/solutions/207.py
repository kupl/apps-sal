class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def canmake(days):
            b = 0
            f = 0

            for d in bloomDay:
                if d <= days:
                    b += (f + 1) // k
                    f = (f + 1) % k
                else:
                    f = 0

            return b >= m

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            mid = (left + right) // 2

            if canmake(mid):
                right = mid
            else:
                left = mid + 1
        return left
