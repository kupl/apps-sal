class Solution:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                idx = i
                break
        if idx == -1:
            return self.bin_search(nums, 0, len(nums), target)
        elif target < nums[0] or target < nums[-1]:
            return self.bin_search(nums, idx, len(nums), target)
        elif target > nums[-1] or target > nums[0]:
            return self.bin_search(nums, 0, idx, target)
        else:
            assert False

    def bin_search(self, nums, i1, i2, target):
        while i1 < i2:
            mi = (i1 + i2) // 2
            if nums[mi] == target:
                return mi
            if nums[mi] > target:
                i2 = mi
            else:
                i1 = mi + 1
        return -1
