class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        ans = sum(abs(nums[i + 1] - nums[i]) for i in range(len(nums) - 1))
        d = 0
        for i in range(1, len(nums) - 1):
            d = max(d, abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]),
                    abs(nums[-1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]))

        high = -math.inf
        low = math.inf
        for x, y in zip(nums, nums[1:]):
            high = max(high, min(x, y))
            low = min(low, max(x, y))
        return ans + max(d, (high - low) * 2)
