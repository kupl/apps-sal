class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        
        left = 1
        right = max(piles)
        
        
        while right > left:
            
            speed = int((left+right)/2)
            
            total_hours = 0
            
            for i in piles:
                total_hours += math.ceil(i/speed)
                
                
            if(total_hours > H):
                left = speed + 1
            else:
                right = speed
                
        return left
                
                
                

