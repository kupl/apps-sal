class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        n = len(nums)
        if n % 2 == 0:
            step1 = max(0, nums[-1] - nums[-2] + 1)
            for i in range(1, n - 1, 2):
                step1 += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
            step2 = max(0, nums[0] - nums[1] + 1)
            for i in range(2, n, 2):
                step2 += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
        else:
            step1 = max(0, nums[-1] - nums[-2] + 1) + max(0, nums[0] - nums[1] + 1)
            for i in range(2, n - 1, 2):
                step1 += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
            step2 = 0
            for i in range(1, n, 2):
                step2 += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
        return min(step1, step2)
