class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def condition(x):
            (currNumFlower, numBouquets) = (0, 0)
            for flower in bloomDay:
                currNumFlower += 1
                if flower > x:
                    currNumFlower = 0
                elif currNumFlower == k:
                    (currNumFlower, numBouquets) = (0, numBouquets + 1)
            if numBouquets >= m:
                return True
            return False
        (left, right) = (1, max(bloomDay) + 1)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left if left > 0 and left < max(bloomDay) + 1 else -1
