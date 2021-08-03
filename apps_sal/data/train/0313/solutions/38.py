class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if k * m > len(bloomDay):
            return -1

        def flowers(days):
            boq, full = 0, 0
            adj = False
            for flower in bloomDay:
                if flower <= days:
                    full += 1
                else:
                    full = 0
                if full == k:
                    full = 0
                    boq += 1
            return boq >= m

        left, right = 0, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if flowers(mid):
                right = mid
            else:
                left = mid + 1
        return left
