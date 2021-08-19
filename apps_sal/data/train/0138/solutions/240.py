class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        l = len(nums)
        pdp = [0] * l
        ndp = [0] * l
        pdp[0] = 1 if nums[0] > 0 else 0
        ndp[0] = 1 if nums[0] < 0 else 0
        b = pdp[0]
        for i in range(1, l):
            n = nums[i]
            if n > 0:
                pdp[i] = max(pdp[i - 1] + 1, 1)
                ndp[i] = ndp[i - 1] + 1 if ndp[i - 1] != 0 else 0
            elif n < 0:
                ndp[i] = max(pdp[i - 1] + 1, 1)
                pdp[i] = ndp[i - 1] + 1 if ndp[i - 1] != 0 else 0
            else:
                pdp[i] = 0
                ndp[i] = 0
            b = max(b, pdp[i])
        return b
