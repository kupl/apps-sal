class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        N = len(nums)
        firstNegIdx = math.inf
        prevZeroIdx = -1
        curr = 1
        res = 0
        for i, n in enumerate(nums):
            if n==0:
                prevZeroIdx = i
                firstNegIdx = math.inf
                curr = 1
            else:
                curr *= n
                if curr>0:
                    res = max(res, i-prevZeroIdx)
                else:
                    firstNegIdx = min(firstNegIdx, i)
                    res = max(res, i-firstNegIdx)
                # print (i, curr, res)
        return res
        # if math.isfinite(res):
        #     return res
        # else:
        #     return 0

