class Solution:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        (low, high) = (0, len(nums) - 1)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        start = low
        (low, high) = (0, len(nums) - 1)
        while low <= high:
            mid = (low + high) // 2
            realMid = (mid + start) % len(nums)
            if nums[realMid] == target:
                return realMid
            if target > nums[realMid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
