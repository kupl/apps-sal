# +60
# +30
# +30
# did not get this one, found the solution in forums
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)
        
        while min_cap < max_cap:
            cap = (min_cap + max_cap) // 2
            
            remainder = cap
            days = 1
            
            for i in range(len(weights)):
                if weights[i] > remainder:
                    remainder = cap
                    days += 1
                    
                remainder -= weights[i]
                
            if days > D:
                min_cap = cap + 1
            else:
                max_cap = cap
                
        
        return min_cap
