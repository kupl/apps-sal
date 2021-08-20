class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        events = sorted(bloomDay)

        def possible(time):
            flower = [j for (j, i) in enumerate(bloomDay) if i <= time]
            left = 0
            bouquets = 0
            for (i, c) in enumerate(flower):
                if i == len(flower) - 1 or flower[i + 1] != c + 1:
                    bouquets += (i - left + 1) // k
                    left = i + 1
            return bouquets >= m
        (lo, hi) = (0, n)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not possible(events[mid]):
                lo = mid + 1
            else:
                hi = mid
        return events[lo] if lo < n else -1
