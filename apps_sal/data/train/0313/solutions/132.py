class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)

        def feasible(day):
            flower = 0
            count = 0
            for bloom in bloomDay:
                if bloom > day:
                    flower = 0
                else:
                    count += (flower + 1) // k
                    flower = (flower + 1) % k

            return count >= m

        if len(bloomDay) < m * k:
            return -1

        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
