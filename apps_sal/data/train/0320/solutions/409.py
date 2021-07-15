class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        res = 0
        n = len(nums)
        
        while True:
            
            p = 0
            for i in range(n):
                if nums[i]%2:
                    nums[i]-=1
                    res += 1
                p+=nums[i]    
            
            if p==0:
                return res
            
            for i in range(n):
                nums[i]//=2
            
            res += 1

    

            
       
                
        
        
        

