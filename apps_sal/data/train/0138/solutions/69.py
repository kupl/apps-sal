class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # if the number of negative numbers is even then we just need to worry about zeroes
        maxLength = 0
        currLength = 0
        negCnt = 0
        negIdxs = []
        head = 0
        for i, n in enumerate(nums):
            if n > 0:
                currLength += 1
                if negCnt%2 == 0:
                    maxLength = max(maxLength, currLength)
            elif n < 0:
                currLength += 1
                negCnt += 1
                negIdxs.append(i)
                if negCnt%2 == 0:
                    maxLength = max(maxLength, currLength)
            if n == 0 or i == len(nums) - 1: # end or 0
                # head and tail?
                if negIdxs:
                    tail = i if n > 0 else i - 1
                    maxLength = max(maxLength, tail - negIdxs[0])
                    # print(negIdxs[-1], head)
                    maxLength = max(maxLength, negIdxs[-1] - head)
                currLength = 0
                negCnt = 0
                negIdxs = []
                head = i + 1
        return maxLength
        
        # negIdx = []
        # zeroIdx = []
        # for i, n in enumerate(nums):
        #     if n < 0:
        #         negIdx.append(i)
        #     elif n == 0:
        #         zeroIdx.append(i)
        # if len(negIdx)%2 == 0:
        #     if len(zeroIdx) == 0:
        #         return len(nums)
        #     else:
        #         for 
        # else:

