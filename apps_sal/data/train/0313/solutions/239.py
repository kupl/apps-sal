class Solution:

    def minDays(self, bloom_day: List[int], m: int, k: int) -> int:

        def bouquets_made(day):
            total = adjacent = 0
            for d in bloom_day:
                if d <= day:
                    adjacent += 1
                else:
                    adjacent = 0
                if adjacent == k:
                    total += 1
                    adjacent = 0
            return total
        min_days = -1
        (lo, hi) = (1, max(bloom_day))
        while lo <= hi:
            mid = (lo + hi) // 2
            if bouquets_made(mid) >= m:
                min_days = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return min_days
