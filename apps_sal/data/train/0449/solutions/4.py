class Solution:

    def findMin(self, nums):
        if len(nums) == 0:
            return -1
        if len(nums) == 2:
            return min(nums)
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low < high:
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            mid = (low + high) // 2
        return nums[low]
        '\n         :type nums: List[int]\n         :rtype: int\n         '
