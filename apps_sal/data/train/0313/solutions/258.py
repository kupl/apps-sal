class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        else:
            left, right = 0, max(bloomDay)
            while left < right:
                mid = (left + right) // 2
                flow, bq = 0, 0
                for d in bloomDay:
                    if d > mid:
                        flow = 0
                    else:
                        flow += 1
                    if flow == k:
                        bq += 1
                        flow = 0
                    if bq == m:
                        break
                if bq == m:
                    right = mid
                else:
                    left = mid + 1
            return left
