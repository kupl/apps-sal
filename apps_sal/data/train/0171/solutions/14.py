class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxPos = nums[0]
        maxNeg = -nums[0]
        p = 1
        result = nums[0]
        while p < len(nums):
            if nums[p] >= 0:
                tmp1 = max(nums[p], nums[p] * maxPos)
                tmp2 = max(-nums[p], nums[p] * maxNeg)
                maxPos = tmp1
                maxNeg = tmp2
            else:
                tmp1 = max(nums[p], -nums[p] * maxNeg)
                tmp2 = max(-nums[p], -nums[p] * maxPos)
                maxPos = tmp1
                maxNeg = tmp2
            print((nums[p], maxPos, maxNeg))
            result = max(result, maxPos)
            p += 1
        return result
