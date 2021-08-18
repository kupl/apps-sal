class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        ans, imp1, min2, max2 = 0, 0, float('inf'), -float('inf')
        for x, y in zip(nums[:-1], nums[1:]):
            ans += abs(x - y)
            imp1 = max(imp1, abs(nums[0] - y) - abs(x - y), abs(nums[-1] - x) - abs(x - y))
            min2, max2 = min(min2, max(x, y)), max(max2, min(x, y))
        return ans + max(imp1, (max2 - min2) * 2)
