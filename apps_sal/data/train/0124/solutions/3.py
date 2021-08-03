class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                left = left + 1

        return False
