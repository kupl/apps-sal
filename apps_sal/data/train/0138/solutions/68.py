class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        p = 1
        j = None
        k = -1
        m = 0
        for (i, n) in enumerate(nums):
            if not n:
                p = 1
                j = None
                k = i
            else:
                if n < 0:
                    p = -p
                if p > 0:
                    m = max(m, i - k)
                elif p < 0:
                    if j is None:
                        j = i
                    else:
                        m = max(m, i - j)
        return m
