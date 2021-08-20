class Solution:

    def minDays(self, bloomDay, m, k):
        (start, end) = (1, max(bloomDay))
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.check(mid, bloomDay, m, k):
                end = mid
            else:
                start = mid
        if self.check(start, bloomDay, m, k):
            return start
        if self.check(end, bloomDay, m, k):
            return end
        return -1

    def check(self, days, bloomDay, m, k):
        cnt = 0
        res = 0
        for d in bloomDay:
            if d <= days:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                res += 1
                cnt = 0
        return res >= m
