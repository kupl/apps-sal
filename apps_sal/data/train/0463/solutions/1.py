class Solution:

    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        gain = 0
        h = float('-inf')
        l = float('inf')
        for i in range(n - 1):
            n1 = nums[i]
            n2 = nums[i + 1]
            s += abs(n1 - n2)
            gain = max(gain, abs(nums[0] - n2) - abs(n1 - n2), abs(nums[n - 1] - n1) - abs(n1 - n2))
            h = max(h, min(n1, n2))
            l = min(l, max(n1, n2))
        return s + max(gain, 2 * (h - l))
