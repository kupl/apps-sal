class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        maxv = float('inf')
        minv = nums[0]
        for num in nums:
            if num > maxv:
                return True
            if num > minv:
                maxv = min(num, maxv)
            minv = min(num, minv)
        return False
