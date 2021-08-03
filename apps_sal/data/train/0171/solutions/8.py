class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = loc_min = loc_max = nums[0]
        for i in nums[1:]:
            if i < 0:
                loc_min, loc_max = loc_max, loc_min
            loc_min = min(i, loc_min * i)
            loc_max = max(i, loc_max * i)
            res = max(loc_min, loc_max, res)
        return res
