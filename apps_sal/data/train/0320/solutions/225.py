class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        
        count_zeros=0
        
        for i in nums:
            if i==0:
                count_zeros+=1
        operations=0
        
        while(count_zeros!=len(nums)):
            
            odd_max=-1
            
            
            for i in range(0,len(nums)):
                if nums[i]%2==1:
                    operations+=1 
                    nums[i]-=1
                    odd_max=i
                    if nums[i]==0:
                        count_zeros+=1
                    
            
            if odd_max==-1:
                operations+=1
                for i in range(0,len(nums)):
                    nums[i]=nums[i]//2
            
            
        return operations
                        
            
        

