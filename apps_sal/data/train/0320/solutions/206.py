class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if max(nums) == 0:
            return 0
        operations = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = nums[i] - 1
                operations += 1
        if operations > 0:
            return operations + self.minOperations(nums)
        for i in range(len(nums)):
            nums[i] = nums[i]//2
        operations += 1
        return operations + self.minOperations(nums)
