class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            temp = self.bouquets(mid, bloomDay, k, m)
            if temp:
                r = mid
            else:
                l = mid + 1
        return l

    def bouquets(self, day, bloomDay, k, m):
        c = 0
        contDays = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] > day:
                contDays = 0
                continue

            contDays += 1
            if contDays == k:
                c += 1
                contDays = 0
        return c >= m
