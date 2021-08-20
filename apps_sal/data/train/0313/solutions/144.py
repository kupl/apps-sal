class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        (start, end) = (1, max(bloomDay))
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.helper(bloomDay, m, k, mid):
                end = mid
            else:
                start = mid
        if self.helper(bloomDay, m, k, start):
            return start
        elif self.helper(bloomDay, m, k, end):
            return end
        else:
            return -1

    def helper(self, bloomDay, m, k, day):
        consecutive = 0
        count = 0
        for bloomday in bloomDay:
            if bloomday > day:
                consecutive = 0
            else:
                consecutive += 1
                if consecutive == k:
                    count += 1
                    consecutive = 0
        return count >= m
