class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        l, r = 1, max(bloomDay)
        while l < r:
            mid = (l + r) // 2

            flow = bouq = 0
            for a in bloomDay:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    bouq += 1
                    flow = 0
                    if bouq == m:
                        break
            if bouq == m:
                r = mid
            else:
                l = mid + 1
        return l
