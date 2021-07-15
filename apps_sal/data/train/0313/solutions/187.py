class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isOK(day, m):
            cur = 0
            for ptr in range(len(bloomDay)):
                if bloomDay[ptr] > day:
                    cur = 0
                else:
                    cur += 1
                    if cur == k:
                        m -= 1
                        cur = 0
                        if m == 0:
                            return True
            return False
            
        if m * k > len(bloomDay):
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if isOK(mid, m):
                right = mid
            else:
                left = mid + 1
        return left
