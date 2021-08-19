class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        steps = 0
        n_zeros = 0
        for (i, num) in enumerate(nums):
            if num % 2 != 0:
                nums[i] -= 1
                steps += 1
            if nums[i] == 0:
                n_zeros += 1
            nums[i] = nums[i] // 2
        if n_zeros != len(nums):
            steps += 1
        return steps + self.minOperations(nums)
