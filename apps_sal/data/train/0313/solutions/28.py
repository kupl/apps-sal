class Solution:

    def minDays(self, bloomDay, m: int, k: int) -> int:
        beg = min(bloomDay)
        end = max(bloomDay)
        n = len(bloomDay)
        res = -1
        while beg <= end:
            mid = beg + int((end - beg) / 2)
            if self.isValid(bloomDay, n, m, k, mid) >= m:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res

    def isValid(self, bloomDay, n, m, k, mx):
        sum = 0
        boquet = 0
        k1 = 0
        for i in range(n):
            k1 += 1
            if bloomDay[i] > mx:
                k1 = 0
            if k1 == k:
                boquet += 1
                k1 = 0
        return boquet
