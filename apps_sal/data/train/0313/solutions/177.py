class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        min_day = bloomDay[0]
        max_day = bloomDay[0]
        for day in bloomDay:
            if min_day > day:
                min_day = day
            if max_day < day:
                max_day = day

        def isValidDay(day_try: int) -> bool:
            count = 0
            current = 0
            for local_day in bloomDay:
                if day_try >= local_day:
                    current += 1
                    if current >= k:
                        count += 1
                        current = 0
                else:
                    current = 0
            return count >= m
        left = min_day
        right = max_day
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if isValidDay(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
