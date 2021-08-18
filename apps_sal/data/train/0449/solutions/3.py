class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        mid = 0
        while left < right:
            mid = left + (right - left) // 2

            if nums[right] < nums[mid]:
                left = mid + 1
            elif nums[right] > nums[mid]:
                if nums[mid - 1] > nums[mid]:
                    return nums[mid]
                else:
                    right = mid - 1
        return nums[left]
