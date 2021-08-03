class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret = 0
        while nums.count(0) != len(nums):
            for i in range(0, len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] = nums[i] - 1
                    ret = ret + 1
            nums[:] = [i / 2 for i in nums]
            ret = ret + 1
        return (0 if ret == 0 else ret - 1)
