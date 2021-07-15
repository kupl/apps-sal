class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count=0
        while sum(nums)!=0:
            for i in range(len(nums)):
                if nums[i]%2!=0:
                    nums[i]-=1
                    count+=1
                    
            for i in range(len(nums)):   
                nums[i]/=2
            if sum(nums)!=0:
                count+=1
            
        return count         
