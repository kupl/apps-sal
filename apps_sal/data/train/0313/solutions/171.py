class Solution:
    def bloom(self, arr, k, d, m):
        cnt, bk = 0, 0
        for i in arr:
            if i <= d:
                cnt += 1
                if cnt == k:
                    bk += 1
                    cnt = 0
            else:
                cnt = 0
        if bk >= m:
            return 1
        else:
            return 0

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = 1
        r = max(bloomDay) + 1
        while l < r:
            mid = (l + r) // 2
            if self.bloom(bloomDay, k, mid, m):
                r = mid
            else:
                l = mid + 1
        return -1 if l > max(bloomDay) else l
