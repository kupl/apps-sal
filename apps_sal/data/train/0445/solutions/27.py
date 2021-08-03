class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        res = float('inf')
        n = len(nums)
        for i in range(4):
            res = min(res, nums[n - 4 + i] - nums[i])
        return res
