class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin, end = 0, 2
        if len(nums) == 1:
            return 0
        while end < len(nums):
            mid = (begin + end) // 2
            if nums[mid] > nums[begin] and nums[mid] > nums[end]:
                return mid
            begin += 1
            end += 1
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
