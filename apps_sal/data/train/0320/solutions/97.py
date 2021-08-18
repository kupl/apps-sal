class Solution:
    def minOperations(self, nums: List[int]) -> int:

        step = 0

        while True:
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] = nums[i] - 1
                    step += 1
                nums[i] = nums[i] // 2
            if sum(nums) == 0:
                return step
            step += 1
