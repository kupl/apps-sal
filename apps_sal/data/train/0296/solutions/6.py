class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            if start < len(nums) - 1 and nums[start] == nums[start + 1]:
                start += 1
                continue
            if nums[end] == nums[end - 1]:
                end -= 1
                continue
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
