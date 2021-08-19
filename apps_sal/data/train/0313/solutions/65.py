class Solution:

    def calc(self, bloomDay, mid, k):
        adj = 0
        totes = 0
        for i in range(len(bloomDay)):
            if adj == k:
                totes += 1
                adj = 0
            if bloomDay[i] <= mid:
                adj += 1
                continue
            adj = 0
        if adj == k:
            totes += 1
        return totes

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        l = 0
        r = max(bloomDay) + 1
        while r - l > 1:
            mid = l + (r - l) // 2
            t = self.calc(bloomDay, mid, k)
            if t >= m:
                r = mid
            elif t < m:
                l = mid
        return r
