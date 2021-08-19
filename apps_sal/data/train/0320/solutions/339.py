class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        while any(nums):
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    ops += 1
            if any(nums):
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
                ops += 1
        return ops
