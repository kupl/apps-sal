class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while (sum(nums)):
            
            for i in range(len(nums)):
                if nums[i]%2 == 1:
                    nums[i] -= 1
                    count += 1
                nums[i] = nums[i]//2
            count += 1
            
        return count - 1
                    
            
                    
        

