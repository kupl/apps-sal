class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r -= 1
        if nums[l] < nums[r]:
            return nums[l]
        else:
            return nums[r]
