class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def can(days):
            res = 0
            count = 0
            for a in bloomDay:
                if a <= days:
                    count += 1
                else:
                    count = 0
                if count == k:
                    count = 0
                    res += 1
            return res >= m

        l, r = 1, max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if can(mid):
                r = mid
            else:
                l = mid + 1
        if can(l):
            return l
        return -1
