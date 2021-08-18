class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        l = 1
        r = max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            flow = 0
            nums = 0
            for i in range(len(bloomDay)):
                if nums >= m:
                    break
                if bloomDay[i] > mid:
                    flow = 0
                else:
                    flow += 1
                    if flow >= k:
                        flow = 0
                        nums += 1
            if nums >= m:
                r = mid
            else:
                l = mid + 1
        return l
