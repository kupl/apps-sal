class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i]%2:
                nums[i] -= 1
                res += 1
        if any(nums):
            nums = [i//2 for i in nums]
            return res + 1 + self.minOperations(nums)
        else:
            return res

