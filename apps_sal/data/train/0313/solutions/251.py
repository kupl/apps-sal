class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if bloomDay == [] or m * k == 0 or len(bloomDay) < m * k:
            return -1
        (left, right) = (1, max(bloomDay))
        while left < right:
            mid = left + (right - left) // 2
            if self.getPossibleBouquetNum(bloomDay, k, mid) >= m:
                right = mid
            else:
                left = mid + 1
        return left

    def getPossibleBouquetNum(self, bloomDay: List[int], k: int, day_threshold: int) -> int:
        bloom_count = 0
        bouquet_count = 0
        for day in bloomDay:
            if day <= day_threshold:
                bloom_count += 1
            else:
                bouquet_count += bloom_count // k
                bloom_count = 0
        bouquet_count += bloom_count // k
        return bouquet_count
