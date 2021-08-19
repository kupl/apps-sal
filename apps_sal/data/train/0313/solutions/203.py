class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def bouqets(d):
            res = 0
            c = 0
            for n in bloomDay:
                if n <= d:
                    c += 1
                else:
                    c = 0
                if c == k:
                    res += 1
                    c = 0
            return res
        days = sorted(set(bloomDay))
        (lo, hi) = (0, len(days) - 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if bouqets(days[mid]) < m:
                lo = mid + 1
            else:
                hi = mid
        return days[hi] if days[hi] >= m else -1
