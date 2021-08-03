class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + ((right - left) // 2)
            m1 = 0
            k1 = 0
            for f in range(len(bloomDay)):
                if bloomDay[f] <= mid:
                    if f == 0 or bloomDay[f - 1] <= mid:
                        k1 += 1
                    else:
                        k1 = 1
                    if k1 == k:
                        m1 += 1
                        k1 = 0
            if m1 >= m:
                right = mid
            else:
                left = mid + 1
        return left
