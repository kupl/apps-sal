class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        ret = 0
        (pos, neg) = (-1, None)
        curr = 1
        for (i, n) in enumerate(nums):
            curr *= n
            if curr == 0:
                (pos, neg) = (i, None)
                curr = 1
            elif curr < 0:
                if neg is None:
                    neg = i
                ret = max(ret, i - neg)
            else:
                ret = max(ret, i - pos)
        return ret
