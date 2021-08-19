class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def bouquets_possible(day):
            bouquets_count = 0
            conse_day = 0
            for (i, v) in enumerate(bloomDay):
                if v <= day:
                    conse_day += 1
                    if conse_day == k:
                        bouquets_count += 1
                        conse_day = 0
                else:
                    conse_day = 0
            return bouquets_count
        if len(bloomDay) < m * k:
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if bouquets_possible(mid) < m:
                left = mid + 1
            else:
                right = mid
        return left
