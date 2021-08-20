class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        l = 1
        r = max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            count = 0
            b = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    count += 1
                if count % k == 0 and count != 0:
                    b += 1
                    count = 0
                if bloomDay[i] > mid:
                    count = 0
            if b >= m:
                r = mid - 1
            else:
                l = mid + 1
        return l
