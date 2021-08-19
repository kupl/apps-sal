class Solution:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[left] > nums[mid]:
                if target < nums[mid] or target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[right] == target:
                return right
            else:
                return -1
        return -1
