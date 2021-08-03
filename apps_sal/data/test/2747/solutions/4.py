class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        a = self.findLeft(nums, target)
        b = self.findRight(nums, target)
        if nums[a] != target:
            return [-1, -1]
        return [a, b]

    def findLeft(self, nums, target):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return low

    def findRight(self, nums, target):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2 + 1
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid
        return high
