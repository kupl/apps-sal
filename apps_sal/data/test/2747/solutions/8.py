class Solution:

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def findBoundary(nums, left, right, target):
            [l_boundary, r_boundary] = [len(nums), -1]
            middle = int((left + right) / 2)
            if left <= right and nums[left] <= target and (nums[right] >= target):
                if nums[left] == target:
                    l_boundary = left
                if nums[right] == target:
                    r_boundary = right
                if nums[middle] < target:
                    [l_boundary, r_boundary] = findBoundary(nums, middle + 1, right, target)
                elif nums[middle] > target:
                    [l_boundary, r_boundary] = findBoundary(nums, left, middle, target)
                else:
                    l_boundary = min(findBoundary(nums, left, middle - 1, target)[0], middle)
                    r_boundary = max(findBoundary(nums, middle + 1, right, target)[1], middle)
            return [l_boundary, r_boundary]
        boundary = findBoundary(nums, 0, len(nums) - 1, target)
        if boundary[1] == -1:
            return [-1, -1]
        else:
            return boundary
