class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = 1, max(bloomDay)
        while l + 1 < r:
            mid = (l + r) // 2
            if self.is_ok(bloomDay, mid, m, k):
                r = mid
            else:
                l = mid
        if self.is_ok(bloomDay, l, m, k):
            return l
        if self.is_ok(bloomDay, r, m, k):
            return r
        return -1

    def is_ok(self, bloomDay, target, m, k):
        flowers = 0
        for remain in bloomDay:
            if remain <= target:
                flowers += 1
                if flowers == k:
                    m -= 1
                    flowers = 0
            else:
                flowers = 0

        return m <= 0
