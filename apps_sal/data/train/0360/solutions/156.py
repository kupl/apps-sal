class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right-left)//2
            
            if self.isFeasible(mid, weights, D):
                right = mid
            else:
                left = mid + 1
            
        return left
    def isFeasible(self, capacity, weights, D):
        
        total = 0
        days = 1
        for weight in weights:
            if total + weight <= capacity:
                
                total += weight
            else:
                total = weight
                days += 1
                if days > D:
                    return False
        return True
            

