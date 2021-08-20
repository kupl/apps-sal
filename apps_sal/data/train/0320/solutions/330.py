class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if set(nums) == set([0]):
            return 0
        ops = 0
        while set(nums) != set([0]):
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    ops += 1
            if set(nums) != set([0]):
                nums = list([x // 2 for x in nums])
                ops += 1
        return ops
