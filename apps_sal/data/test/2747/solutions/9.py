class Solution:

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        (l, r) = (0, len(nums) - 1)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        left = l if nums[l] == target else r
        (l, r) = (0, len(nums) - 1)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        right = r if nums[r] == target else l
        if nums[left] != target:
            return [-1, -1]
        return [left, right]
