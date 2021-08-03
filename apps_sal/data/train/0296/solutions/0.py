class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end = end - 1
        return nums[start]
