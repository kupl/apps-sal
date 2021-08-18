class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0:
            return null
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0

        for ind in range(1, len(nums) - 1):
            print(ind)

            if nums[ind] > nums[ind - 1] and nums[ind] > nums[ind + 1]:
                return ind

        if nums[n - 1] > nums[n - 2]:
            print('haha')
            return n - 1
