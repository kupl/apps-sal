class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def check(bloomDay, day, m, k):
            count = 0
            for flower in bloomDay:
                if flower <= day:
                    count += 1
                    if count == k:
                        m -= 1
                        count = 0
                    if m == 0:
                        return True
                else:
                    count = 0
            return False
        start = min(bloomDay)
        end = max(bloomDay)
        res = -1
        while start <= end:
            center = start + (end - start) // 2
            if check(bloomDay, center, m, k):
                res = center
                end = center - 1
            else:
                start = center + 1
        return res
