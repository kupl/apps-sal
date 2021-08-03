class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # m = nums[0]
        # for num in nums:
        #     if num < m:
        #         m = num
        # return m
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return nums[i]

        return nums[0]
