class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        n = len(bloomDay)
        if n < m * k:
            return -1

        def check(x):
            cnt = 0
            i = 0
            for day in bloomDay:
                if day <= x:
                    i += 1
                    if i == k:
                        cnt += 1
                        i = 0
                    if cnt == m:
                        return True
                else:
                    i = 0
            return False

        days = sorted(set(bloomDay))

        lo, hi = 0, len(days) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if check(days[mid]):
                hi = mid
            else:
                lo = mid + 1
        return days[hi] if check(days[hi]) else -1
