class Solution:

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        lo = bisect.bisect_left(nums, target)
        if target in nums[lo:lo + 1]:
            hi = bisect.bisect(nums, target) - 1
            return [lo, hi]
        else:
            return [-1, -1]
