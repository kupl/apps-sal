class Solution:

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] == nums[i + 1]:
                return nums[i]
            i += 1
