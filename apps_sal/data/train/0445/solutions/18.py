class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums = sorted(nums)
        (l, r) = (0, len(nums) - 1)
        res = nums[-1] - nums[0]
        for i in range(0, 4):
            res = min(res, nums[-4 + i] - nums[i])
        return res
