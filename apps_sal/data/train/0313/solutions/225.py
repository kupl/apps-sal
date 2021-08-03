class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            flowers = 0
            bouquets = 0
            for day in bloomDay:
                flowers = flowers + 1 if day <= mid else 0
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            if bouquets < m:
                left = mid + 1
            else:
                right = mid
        return left
