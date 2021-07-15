class Solution:
    def get_day(self, weights, cap):
        i = 0
        res = 0
        wei = 0
        while i < len(weights): 
            if wei + weights[i] <= cap:
                    wei += weights[i]
                    i += 1
            else:
                wei = 0
                res += 1
        return res + 1
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        
        
                
        
        
        start, end = max(weights), sum(weights)
        
        while start < end:
            mid = (start + end) // 2
            
            days=self.get_day(weights,mid)
            if days <= D:
                end = mid
            else:
                start = mid + 1
             
              
        return end 
        
        
            
        

