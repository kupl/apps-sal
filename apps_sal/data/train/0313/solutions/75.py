from functools import reduce


class Solution:

    def valid(self, bloomDay, k, m, mid):
        (i, n) = (0, len(bloomDay))
        while i + k - 1 < n:
            j = i
            while j < n and j < i + k:
                if bloomDay[j] > mid:
                    i = j + 1
                    break
                j += 1
            else:
                m -= 1
                i = j
            if m <= 0:
                return True
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        (l, r) = reduce(lambda a, b: (min(a[0], b), max(a[1], b)), bloomDay, (float('inf'), float('-inf')))
        while l < r:
            mid = (l + r - 1) // 2
            v = self.valid(bloomDay, k, m, mid)
            if v:
                r = mid
            else:
                l = mid + 1
        return r
