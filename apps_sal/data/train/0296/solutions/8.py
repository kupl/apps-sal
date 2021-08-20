class Solution:

    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        res = nums[r]
        while l < r:
            if nums[l] < nums[r]:
                return min(nums[l], res)
            res = min(res, nums[r])
            m = int((l + r) / 2)
            if nums[l] == nums[r]:
                temp = nums[r]
                while nums[l] == temp and l < r:
                    l = l + 1
                while nums[r] == temp and l < r:
                    r = r - 1
            elif nums[m] >= nums[l]:
                l = m + 1
            elif nums[m] <= nums[r]:
                res = min(nums[m], res)
                r = m - 1
        return min(nums[l], res)
        '\n         :type nums: List[int]\n         :rtype: int\n         '
