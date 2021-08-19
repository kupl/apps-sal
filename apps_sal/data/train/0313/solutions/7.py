class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def bouquet_count(t):
            count = 0
            res = 0
            for i in range(n):
                if bloomDay[i] <= t:
                    count += 1
                    if count == k:
                        count = 0
                        res += 1
                else:
                    count = 0
            return res
        n = len(bloomDay)
        if m * k > n:
            return -1
        (low, high) = (min(bloomDay), max(bloomDay))
        while low <= high:
            mid = low + (high - low) // 2
            if bouquet_count(mid) >= m:
                high = mid - 1
            else:
                low = mid + 1
        return low
