class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        totol, res, min2, max2 = 0, 0, float('inf'), -float('inf')
        for a, b in zip(nums, nums[1:]):
            totol += abs(a - b)
            res = max(res, abs(nums[0] - b) - abs(a - b))
            res = max(res, abs(nums[-1] - a) - abs(a - b))
            min2, max2 = min(min2, max(a, b)), max(max2, min(a, b))
        return totol + max(res, (max2 - min2) * 2)
