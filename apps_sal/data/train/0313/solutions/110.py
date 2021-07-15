class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            cnt, n = 0, 0
            for b in bloomDay:
                if b <= mid:
                    n += (cnt + 1) // k
                    if n == m:
                        break
                    cnt = (cnt + 1) % k
                else:
                    cnt = 0
            if n == m:
                right = mid
            else:
                left = mid + 1
        return left
