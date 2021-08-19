class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        numNeg = 0
        numZero = 0
        negOddPos = -1
        negEvenPos = -1
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                numNeg += 1
            if nums[i] == 0:
                negOddPos = -1
                negEvenPos = -1
                numZero += 1
            if numNeg % 2 == 0 and negEvenPos < 0:
                negEvenPos = i
            if numNeg % 2 == 1 and negOddPos < 0:
                negOddPos = i
            if nums[i] != 0:
                if numNeg % 2 == 0 and negEvenPos >= 0:
                    maxlen = max(maxlen, i - negEvenPos)
                if numNeg % 2 == 1 and negOddPos >= 0:
                    maxlen = max(maxlen, i - negOddPos)
                if numZero == 0 and numNeg % 2 == 0:
                    maxlen = max(maxlen, i + 1)
        return maxlen
