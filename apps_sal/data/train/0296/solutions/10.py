class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        minimun = nums[0]
        for i in range(0, len(nums) - 1):
            if nums[i + 1] >= nums[i]:
                continue
            else:
                minimun = nums[i + 1]
        return minimun
