class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)

        s = 0
        for i in range(len(nums) - 1):
            s += abs(nums[i] - nums[i + 1])

        if n <= 2:
            return s

        maxup = inc = 0
        minmax = float('inf')
        maxmin = -float('inf')
        for left in range(1, n):
            dis = abs(nums[left] - nums[left - 1])
            minmax = min(minmax, max(nums[left], nums[left - 1]))
            maxmin = max(maxmin, min(nums[left], nums[left - 1]))
            inc = max(inc, abs(nums[0] - nums[left]) - dis)
            inc = max(inc, abs(nums[-1] - nums[left - 1]) - dis)

        return s + max(inc, 2 * (maxmin - minmax))
