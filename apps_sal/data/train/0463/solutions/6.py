class Solution:

    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        ans = 0
        for i in range(1, n - 1):
            ans = max(ans, abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]), abs(nums[-1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]))
        (small, large) = ((-1, float('inf')), (-1, -float('inf')))
        for i in range(n):
            if i >= 1:
                if nums[i] >= nums[i - 1]:
                    if small[1] > nums[i]:
                        small = (i, nums[i])
                if nums[i] <= nums[i - 1]:
                    if large[1] < nums[i]:
                        large = (i, nums[i])
            if i < n - 1:
                if nums[i] >= nums[i + 1]:
                    if small[1] > nums[i]:
                        small = (i, nums[i])
                if nums[i] <= nums[i + 1]:
                    if large[1] < nums[i]:
                        large = (i, nums[i])
        return sum([abs(nums[i] - nums[i + 1]) for i in range(n - 1)]) + max(2 * (large[1] - small[1]), 0, ans)
