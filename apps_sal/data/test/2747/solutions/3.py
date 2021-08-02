

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) == 0:
            return [-1, -1]

        nums = [target - 1] + nums + [target + 1]

        lbound = -1

        l, r = 1, len(nums) - 2

        while l <= r:

            m = (l + r)//2

            if nums[m] == target and nums[m - 1] < target:
                lbound = m
                break

            if nums[m] < target:
                l = m + 1
            else: # nums[m] >= target:
                r = m - 1

        if lbound == -1:
            return [-1, -1]

        rbound = -1
        l, r = 1, len(nums) - 2

        while l <= r:

            m = (l + r)//2

            if nums[m] == target and nums[m + 1] > target:
                rbound = m
                break

            if nums[m] <= target:
                l = m + 1
            else: # target < nums[m]
                r = m - 1

        return [lbound - 1, rbound - 1]

