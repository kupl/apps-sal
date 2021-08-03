class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        lo, hi = min(bloomDay), max(bloomDay)

        def validDay(bloom, day):
            cnt, adj = 0, 0
            for b in bloom:
                if b <= day:
                    adj += 1
                if adj >= k:
                    adj = 0
                    cnt += 1
                if b > day:
                    adj = 0
            print((cnt, k))
            return cnt >= m
        while lo < hi:
            mid = (lo + hi) // 2
            if validDay(bloomDay, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
