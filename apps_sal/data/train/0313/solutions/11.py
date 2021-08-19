class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        n = len(bloomDay)

        def counter(day, k):
            (count, bouquets) = (0, 0)
            for i in range(n):
                if bloomDay[i] <= day:
                    count += 1
                else:
                    count = 0
                if count == k:
                    bouquets += 1
                    count = 0
            return bouquets
        (low, high) = (1, max(bloomDay))
        while low < high:
            mid = (low + high) // 2
            if counter(mid, k) >= m:
                high = mid
            else:
                low = mid + 1
        return low
