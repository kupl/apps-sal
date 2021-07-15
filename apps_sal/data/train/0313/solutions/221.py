class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if not self.check(bloomDay, m, k, mid):
                l = mid + 1
            else:
                r = mid
        if self.check(bloomDay, m, k, l):
            return l
        return -1
    
    def check(self, bloomDay, m, k, day):
        cnt, consecutive = 0, 0
        for bd in bloomDay:
            if bd <= day:
                consecutive += 1
                if consecutive >= k:
                    cnt += 1
                    if cnt >= m:
                        return True
                    consecutive = 0
            else:
                consecutive = 0
        return False
