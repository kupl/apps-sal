class Solution:

    def minOperations(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        if arr == nums:
            return 0
        ops = 0
        while arr != nums:
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    ops += 1
            ops += 1
            nums = [x / 2 for x in nums]
        return ops - 1
