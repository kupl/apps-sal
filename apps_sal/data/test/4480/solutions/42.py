class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        totalSum = sum(A)
        if totalSum % 3 != 0:
            return False
        target = totalSum // 3
        numPartitions = 0
        currSum = 0
        for num in A:
            currSum += num
            if currSum == target:
                numPartitions += 1
                currSum = 0
                if numPartitions == 3:
                    return True
        return False
