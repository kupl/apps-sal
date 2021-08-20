class Solution:

    def check(self, arr, val):
        total = 0
        for (i, value) in enumerate(arr):
            if value >= val:
                return total + (len(arr) - i) * val
            total += value
        return total

    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        hi = max(arr)
        lo = 0
        mid = (lo + hi) // 2
        limit = hi
        low_value = abs(self.check(arr, hi) - target)
        while lo <= hi:
            calculated_value = self.check(arr, mid)
            if calculated_value >= target:
                hi = mid - 1
            if calculated_value <= target:
                lo = mid + 1
            diff = abs(calculated_value - target)
            if diff < low_value or (diff == low_value and mid < limit):
                limit = mid
                low_value = diff
            mid = (hi + lo) // 2
        return limit

    def findBestValue_fast(self, arr, target):
        arr.sort()
        ilen = len(arr)
        for i in arr:
            ideal = round(target / ilen)
            if ideal <= i:
                return ideal
            target -= i
            ilen -= 1
        return arr[-1]
