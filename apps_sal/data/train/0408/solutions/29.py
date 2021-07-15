class Solution:
    def check(self, arr, val):
        result = 0
        for value in arr:
            result += min(value, val)
        return result
        
    def findBestValue(self, arr: List[int], target: int) -> int:
        hi = max(arr)
        lo = 0
        mid = (lo+hi) // 2
        
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

