class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def make_boquets(mid):
            (flowers, bouquets) = (0, 0)
            for flower in bloomDay:
                if flower > mid:
                    flowers = 0
                else:
                    flowers += 1
                    if flowers == k:
                        flowers = 0
                        bouquets += 1
            return bouquets >= m
        (left, right) = (min(bloomDay), max(bloomDay) + 1)
        while left < right:
            mid = left + (right - left) // 2
            if make_boquets(mid):
                right = mid
            else:
                left = mid + 1
        if left > max(bloomDay):
            return -1
        return left
