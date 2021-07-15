class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count=0
        while sum(nums)>0:
            for i in range(len(nums)):
                count += nums[i] % 2
                nums[i] = nums[i] // 2
                
            if sum(nums)>0: count += 1
                
        return count
