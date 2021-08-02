class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:

        sumA = sum(A)
        if sumA % 3 != 0:
            return False
        tmpSum, isFound, eachPart = 0, 0, sumA // 3
        for i in A:
            tmpSum += i
            if tmpSum == eachPart:
                tmpSum = 0
                isFound += 1
        if isFound >= 3:
            return True
        else:
            return False
