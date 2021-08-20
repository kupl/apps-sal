class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        firstNeg = -1
        zeroPos = -1
        cnt = 0
        ret = 0
        for (i, n) in enumerate(nums):
            if n < 0:
                cnt += 1
                if firstNeg == -1:
                    firstNeg = i
            elif not n:
                (firstNeg, cnt) = (-1, 0)
                zeroPos = i
            if cnt % 2:
                ret = max(ret, i - firstNeg)
            else:
                ret = max(ret, i - zeroPos)
        return ret
