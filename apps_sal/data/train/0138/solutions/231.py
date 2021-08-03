class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        numPos, numNeg, res = 0, 0, 0

        for i in range(len(nums)):
            if nums[i] > 0:
                numPos += 1
                if numNeg > 0:
                    numNeg += 1
            elif nums[i] < 0:
                numPosTmp, numNegTmp = numPos, numNeg
                if numPosTmp > 0:
                    numNeg = numPosTmp + 1
                else:
                    numNeg = 1
                if numNegTmp > 0:
                    numPos = numNegTmp + 1
                else:
                    numPos = 0
            else:
                numNeg = 0
                numPos = 0
            res = max(res, numPos)
        return res
