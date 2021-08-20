class Solution:

    def checkL(self, arr, t, k):
        ans = 0
        temp = 0
        for (i, n) in enumerate(arr):
            if t >= n:
                temp += 1
            else:
                ans += temp // k
                temp = 0
        ans += temp // k
        return ans

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = min(bloomDay)
        r = max(bloomDay)
        mm = r
        while l <= r:
            mid = (l + r) // 2
            if self.checkL(bloomDay, mid, k) >= m:
                r = mid - 1
            elif self.checkL(bloomDay, mid, k) < m:
                l = mid + 1
        if l == mm + 1:
            return -1
        return l
