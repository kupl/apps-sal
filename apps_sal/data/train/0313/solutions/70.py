class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            flower, bouquet = 0, 0
            for b in bloomDay:
                flower = 0 if b > mid else flower + 1
                if flower >= k:
                    flower = 0
                    bouquet += 1
                    if bouquet == m:
                        break
            if bouquet == m:
                right = mid
            else:
                left = mid + 1
        return left
