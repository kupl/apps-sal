class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        ret = 0
        (pos, neg) = (-1, None)
        curr = 0
        for (i, n) in enumerate(nums):
            if n == 0:
                (pos, neg) = (i, None)
                curr = 0
            else:
                if n < 0:
                    curr = 1 - curr
                if curr == 0:
                    ret = max(ret, i - pos)
                if curr == 1:
                    if neg is not None:
                        ret = max(ret, i - neg)
                    else:
                        neg = i
        return ret
