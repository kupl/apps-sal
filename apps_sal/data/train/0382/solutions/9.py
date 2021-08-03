class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return 0

        l, r = 0, len(nums)
        while l < r:
            if l == r:
                break
            m = (l + r) // 2

            if m < len(nums) - 1 and nums[m] > nums[m + 1]:
                if nums[m] >= nums[m - 1]:
                    return m

            if m < len(nums) - 1 and nums[m] < nums[m + 1] and nums[m - 1] < nums[m]:
                l = m + 1
            else:
                r = m

        if l > 0:
            if nums[l] > nums[l - 1]:
                return l
            else:
                return l - 1
        elif nums[l] > nums[l + 1]:
            return l
        else:
            return l + 1
