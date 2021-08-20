class Solution:

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
            if n < 0:
                i = -n
            else:
                i = n
            ind = i - 1
            if nums[ind] < 0:
                return i
            else:
                nums[ind] = -nums[ind]
        return extra
