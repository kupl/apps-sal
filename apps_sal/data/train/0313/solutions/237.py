class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMake(bloomDay, m, k, day):
            cur, cnt = 0, 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    cur += 1
                    if cur == k:
                        cnt += 1
                        cur = 0
                        if cnt == m:
                            return True
                else:
                    cur = 0
            return False
        if m * k > len(bloomDay):
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if not canMake(bloomDay, m, k, mid):
                left = mid + 1
            else:
                right = mid
        return left
