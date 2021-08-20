class Solution:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        (l, r) = (0, len(nums) - 1)
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            while nums[mid] == nums[r]:
                r -= 1
                mid = l + (r - l) // 2
                if r < 0:
                    return False
            if nums[mid] == target:
                return True
            if nums[mid] <= nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif target < nums[mid] and target >= nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        return False
