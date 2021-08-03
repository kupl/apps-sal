class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid - 1]:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    start = mid
            else:
                end = mid
        if nums[start] > nums[end]:
            return start
        else:
            return end
