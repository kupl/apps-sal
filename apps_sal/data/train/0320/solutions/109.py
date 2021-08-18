class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0 and nums[i] > 0:
                count += 1
                nums[i] -= 1
        if nums == [0] * len(nums):
            return count
        nums = [i // 2 for i in nums]
        return count + self.minOperations(nums) + 1
