class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def days_taken(capacity, arr):
            days = 0
            i = 0
            while i < len(arr):
                j = i
                bucket = capacity
                days += 1
                while j < len(arr) and arr[j] <= bucket and bucket > 0:
                    bucket -= arr[j]
                    j += 1
                i = j
            return days
        
        low = max(weights)
        high = sum(weights)
        
        
        
        while low < high:
            mid = (low + high) // 2
            days_by_mid = days_taken(mid, weights)
            
            if days_by_mid <= D:
                high = mid
            else:
                low = mid + 1
        
        return low
        
        
        

