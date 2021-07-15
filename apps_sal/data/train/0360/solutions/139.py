class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def feasible(capacity):
            day = 1
            total = 0
            
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    day += 1
                    
                    if day > D:
                        return False
                
            
            return True
        
        low, high = max(weights), sum(weights)
        
        while low < high:
            mid = low + (high-low)//2
            
            if feasible(mid):
                high = mid
            
            else:
                low = mid+1
            
        return low
