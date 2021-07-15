class Solution:
    def minOperations(self, nums: List[int]) -> int:
        minops = 0
        while sum(nums)>0:
            for i,num in enumerate(nums):
                if num&1: 
                    nums[i] -= 1
                    minops += 1
            nums = [num>>1 for num in nums]
            minops += 1
        return minops-1

