class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)
        left = 1
        right = sum(weights)
        
        def works(capacity):
            tot_days = 0
            i = 0
            
            while i < n:
                j = i
                curr_load = 0
                
                while j < n and curr_load + weights[j] <= capacity:
                    curr_load += weights[j]
                    j += 1
                    
                if j == i:
                    return False
                
                i = j
                tot_days += 1
                
            return tot_days <= D
            
        while left <= right:
            mid = (left + right) // 2
            
            if works(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
