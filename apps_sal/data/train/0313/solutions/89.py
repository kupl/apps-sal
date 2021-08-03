class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        left, right = min(bloomDay), max(bloomDay)

        def condition(day):
            counter = 0
            res = 0
            for d in bloomDay:
                if d <= day:
                    counter += 1
                else:
                    counter = 0
                if counter >= k:
                    res += 1
                    counter = 0
            return res >= m
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
