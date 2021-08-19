class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        s = 0
        e = max(bloomDay)
        ans = -1
        while s <= e:
            mid = int(s + (e - s) / 2)
            if self.checkDay(bloomDay, m, k, mid):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        return ans

    def checkDay(self, a, m, k, d):
        tot = 0
        count = 0
        for i in range(len(a)):
            if a[i] <= d:
                count += 1
                if count == k:
                    tot += 1
                    count = 0
            else:
                count = 0
        return tot >= m
