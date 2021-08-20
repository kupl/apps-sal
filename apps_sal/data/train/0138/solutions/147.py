class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        lastExtraMinus = None
        lastZero = 0
        out = 0
        firstExtraMinus = None
        for (i, n) in enumerate(nums):
            if n < 0:
                lastExtraMinus = None if lastExtraMinus != None else i
                if firstExtraMinus == None:
                    firstExtraMinus = i
            if n == 0:
                lastZero = i + 1
                lastExtraMinus = None
                firstExtraMinus = None
            elif lastExtraMinus == None:
                out = max(out, i - lastZero + 1)
            else:
                out = max(out, i - firstExtraMinus)
        return out
