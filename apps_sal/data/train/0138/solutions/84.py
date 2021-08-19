class Solution:

    def getMaxLen(self, nums):
        n = len(nums)
        (pos, neg) = (0, 0)
        res = 0
        for i in range(n):
            if nums[i] > 0:
                (pos, neg) = (1 + pos, 1 + neg if neg else 0)
            elif nums[i] < 0:
                (pos, neg) = (1 + neg if neg else 0, 1 + pos)
            else:
                (pos, neg) = (0, 0)
            res = max(res, pos)
        return res
