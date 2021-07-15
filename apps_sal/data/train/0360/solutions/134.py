class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        l,h = max(weights),sum(weights)
        
        
        while l < h:
            
            
            days = 1
            
            total_weight = 0
            
            capacity = (l+h)//2
            # print(capacity)
            
            for weight in weights:
                total_weight += weight
                
                if total_weight > capacity:
                    # print(total_weight)
                    days += 1
                    total_weight = weight
            if days <= D:
                h = capacity
            else:
                l = capacity+1
        return l
                    
            # print(days,total_weight)
            # break
                    
                

