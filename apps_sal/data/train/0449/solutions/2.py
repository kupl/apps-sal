class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        start, end = 0, len(nums) - 1
        target = nums[-1]

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                end = mid
            else:
                start = mid

        if nums[start] < target:
            return nums[start]
        return nums[end]
