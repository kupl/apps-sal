class Solution:

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = 99999999999
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1] and min > nums[i + 1]:
                min = nums[i + 1]
            elif nums[i] <= nums[i + 1] and min > nums[i]:
                min = nums[i]
        return min
