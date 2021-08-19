class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def validable(days):
            bloom = 0
            bouquet = 0
            for b in bloomDay:
                if b <= days:
                    bloom += 1
                    bouquet += bloom // k
                    bloom = bloom % k
                else:
                    bloom = 0
            return bouquet >= m
        if len(bloomDay) < m * k:
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if validable(mid):
                right = mid
            else:
                left = mid + 1
        return left
