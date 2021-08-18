class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            v = nums[m]
            if nums[m - 1] < v:
                if nums[r] > v:
                    r = m - 1
                else:
                    l = m + 1
            else:
                l = m + 1

        if l == r:
            if m < l:
                if nums[m] < nums[l]:
                    return nums[m]
                else:
                    return nums[l]
        if l < m:
            if nums[l - 1] < nums[m]:
                return nums[l - 1]
            return nums[l]
        elif r < l:
            return nums[r]
        else:
            return nums[m]

    def findMin_PASSED(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        retval = float('inf')
        l, r = 0, len(nums) - 1
        while l < r:

            m = (l + r) // 2
            v = nums[m]

            if v < nums[m + 1]:
                if v < nums[r]:
                    r = m
                elif v > nums[r]:
                    l = m + 1
            elif v > nums[m + 1]:
                l = m + 1

        if nums[m] < nums[m + 1]:
            return nums[m]
        else:
            return nums[m + 1]
