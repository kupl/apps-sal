class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        partSum = sum(A) / 3
        curSum = 0
        partNum = 0
        for i in A:
            curSum += i
            if curSum == partSum:
                curSum = 0
                partNum += 1
        if partSum == 0:
            return partNum >= 3
        else:
            return partNum == 3
