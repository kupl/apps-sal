class Solution:
    def minOperations(self, nums: List[int]) -> int:
        zeros = []
        operations = 0
        for item in nums:
            zeros.append(0)
        
        while nums != zeros:
            for index,item in enumerate(nums):
                if item%2==1:
                    nums[index]=item-1
                    operations +=1
                    
            if nums==zeros:
                break 
            for index, item in enumerate(nums):
                if item%2==0:
                    nums[index] = item/2
            operations +=1 
        
        return operations
            
            
                
                
            
            
            
            
        
                
                    
                    
                
                    
            
            
    
            
        
        

