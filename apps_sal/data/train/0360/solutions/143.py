class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def feasible(capacity):
            
            days = 1
            total = 0
            for weight in weights:
                total += weight
                
                if total > capacity:
                    total = weight
                    days += 1
                    if days > D:
                        return False
            return True
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right - left)//2
            
            if feasible(mid):
                right = mid
            else:
                left = mid+1
                
        return left
