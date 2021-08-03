class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            return min(nums)
        lo = 0
        hi = len(nums) - 1
        mid = (hi + lo) // 2
        if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
            return nums[mid]
        if nums[mid] > nums[lo] and nums[mid] > nums[hi]:
            # pivot on the right side
            return self.findMin(nums[mid:])
        # elif nums[mid] < nums[lo] and nums[mid] < nums[hi]:
        else:
            # pivot on the left side
            return self.findMin(nums[:mid + 1])
