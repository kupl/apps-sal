class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        result = nums[-1] - nums[0]
        x = min(4, len(nums))
        for i in range(x):
            curr = nums[-x + i] - nums[i]
            result = min(result, curr)
        return result
