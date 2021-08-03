class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(day):
            i = temp = b = 0
            while i < len(bloomDay):
                if bloomDay[i] <= day:
                    temp += 1
                    if temp == k:
                        b += 1
                        temp = 0
                        if b >= m:
                            return True
                else:
                    temp = 0
                i += 1
            return False

        if len(bloomDay) < m * k:
            return -1

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left
