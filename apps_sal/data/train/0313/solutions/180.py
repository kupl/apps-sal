class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        (lo, hi) = (min(bloomDay), max(bloomDay))
        while lo < hi:
            mid = (lo + hi) // 2
            (i, cap, bqts) = (0, 0, 0)
            while i < len(bloomDay):
                if bloomDay[i] <= mid:
                    cap += 1
                else:
                    cap = 0
                if cap == k:
                    bqts += 1
                    cap = 0
                i += 1
            if bqts < m:
                lo = mid + 1
            else:
                hi = mid
        return lo
