class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        fpos = -1
        fneg = -1
        best = 0
        cur = 1
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                fpos = i
                fneg = -1
                cur = 1
            else:
                if fneg == -1 and n < 0:
                    fneg = i
                cur *= n
                if cur > 0:
                    best = max(best, i - fpos)
                elif cur < 0 and fneg != -1:
                    best = max(best, i - fneg)
        return best
