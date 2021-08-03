class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def make_boquets(mid):
            i, boquets = 0, 0
            while i < len(bloomDay):
                j = i
                while j < len(bloomDay) and j - i < k:
                    if bloomDay[j] > mid:
                        break
                    j += 1
                if j - i == k:
                    boquets += 1
                    j -= 1
                i = j + 1
            return boquets >= m
        left, right = min(bloomDay), max(bloomDay) + 1
        while left < right:
            mid = left + (right - left) // 2
            if make_boquets(mid):
                right = mid
            else:
                left = mid + 1
        if left > max(bloomDay):
            return -1
        return left
