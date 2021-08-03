class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        l = 0
        r = len(nums) - 1
        print((">", l, r))
        while l < r and nums[l] == nums[r]:
            l = l + 1
        while l <= r:
            mid = int((l + r + 1) / 2)
            if target == nums[mid]:
                return True
            if target < nums[mid]:
                if target == nums[l]:
                    return True
                elif target > nums[l]:
                    r = mid - 1
                elif target < nums[l]:
                    if nums[l] <= nums[mid]:
                        l = mid + 1
                    elif nums[l] > nums[mid]:
                        r = mid - 1
            if target > nums[mid]:
                if target == nums[r]:
                    return True
                elif target > nums[r]:
                    if nums[mid] >= nums[l]:
                        l = mid + 1
                    elif nums[mid] < nums[l]:
                        r = mid - 1
                elif target < nums[r]:
                    l = mid + 1
        return False
