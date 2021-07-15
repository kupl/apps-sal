class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left = 1
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            flow = 0
            bouq = 0
            for n in bloomDay:
                if n > mid:
                    flow = 0
                else:
                    flow += 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m:
                        break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left
