class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        lo = 1
        hi = max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.can_make(mid, bloomDay, m, k):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def can_make(self, day, bloomDay, m, k):
        cnt = 0
        for d in bloomDay:
            if d <= day:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                m -= 1
                cnt = 0
            if m == 0:
                return True
        return m == 0
