class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def bouqets(d):
            (res, c) = (0, 0)
            for n in bloomDay:
                c = 0 if n > d else c + 1
                if c == k:
                    (res, c) = (res + 1, 0)
            return res
        days = sorted(set(bloomDay))
        (lo, hi) = (0, len(days) - 1)
        while lo < hi:
            mid = (lo + hi) // 2
            (bouq, c) = (0, 0)
            for n in bloomDay:
                c = 0 if n > days[mid] else c + 1
                if c == k:
                    (bouq, c) = (bouq + 1, 0)
            if bouq < m:
                lo = mid + 1
            else:
                hi = mid
        return days[hi] if bouqets(days[hi]) >= m else -1
