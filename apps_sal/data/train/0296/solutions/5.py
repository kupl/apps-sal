class Solution:

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        for index in range(-1, len(nums) - 1):
            if nums[index] > nums[index + 1]:
                return nums[index + 1]
            if index + 1 == len(nums) - 1:
                return nums[0]
        return None
