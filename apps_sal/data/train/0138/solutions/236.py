class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        (pos, neg) = (-1, n)
        c = 1
        ret = 0
        for (i, j) in enumerate(nums):
            if j == 0:
                (pos, neg) = (i, n)
                c = 1
                continue
            if j > 0:
                pass
            else:
                c *= -1
            if c == 1:
                ret = max(ret, i - pos)
            else:
                ret = max(ret, i - neg)
                neg = min(neg, i)
        return ret
