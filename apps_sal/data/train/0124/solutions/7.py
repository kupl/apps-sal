class Solution:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        (start, end) = (0, len(nums) - 1)
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            while start <= end and nums[start] == nums[end]:
                if nums[start] == target:
                    return True
                start += 1
                end -= 1
            if start > end:
                return False
            if nums[start] < nums[end]:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[start]:
                if target < nums[mid] or target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif target > nums[mid] or target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return False
