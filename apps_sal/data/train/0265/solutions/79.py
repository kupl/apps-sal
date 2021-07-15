class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        
        d = {0:1}
        
        total = 0
        count = 0
        
        for i in nums:
            total += i
            
            
            if total - target in d:
                print(total)
                count += 1
                d = {0:1}
                total = 0
            
            else :
                d[total] = 1
                
        return count
        
        
            
        
        
        
        
        

