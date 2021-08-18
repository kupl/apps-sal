class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxLength = 0
        currLength = 0
        negCnt = 0
        negIdxs = []
        head = 0
        for i, n in enumerate(nums):
            if n > 0:
                currLength += 1
                if negCnt % 2 == 0:
                    maxLength = max(maxLength, currLength)
            elif n < 0:
                currLength += 1
                negCnt += 1
                negIdxs.append(i)
                if negCnt % 2 == 0:
                    maxLength = max(maxLength, currLength)
            if n == 0 or i == len(nums) - 1:
                if negIdxs:
                    tail = i if n > 0 else i - 1
                    maxLength = max(maxLength, tail - negIdxs[0])
                    maxLength = max(maxLength, negIdxs[-1] - head)
                currLength = 0
                negCnt = 0
                negIdxs = []
                head = i + 1
        return maxLength
