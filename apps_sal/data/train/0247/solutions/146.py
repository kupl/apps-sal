class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefixSum = [0] * n
        targetSum = [sys.maxsize] * n
        beforeSum = [sys.maxsize] * n
        afterSum = [sys.maxsize] * n
        sumDict = {0:-1}
        total = 0
        for i in range(n):
            total += arr[i]
            prefixSum[i] = total
            if (total - target) in sumDict:
                index = sumDict[total - target]
                targetSum[i] = i - index
            sumDict[total] = i

        minValue = sys.maxsize
        for i in range(n):
            # if (targetSum[i] > 0):
            minValue = min(targetSum[i], minValue)
            beforeSum[i] = minValue

        minValue = sys.maxsize
        for i in reversed(list(range(1, n))):
            # print(targetSum[i])
            startIndex = i - targetSum[i]
            if (startIndex >= 0):
                afterSum[startIndex] = min(afterSum[startIndex], targetSum[i])
                # print(f\"Setting aftersum[{startIndex}] = {afterSum[startIndex]}\")
            # minValue = min(targetSum[i], minValue)
            # afterSum[i - 1] = minValue
                
        # print(f\"targetSum = {targetSum}\")
        # print(f\"afterSum = {afterSum}\")
        # print(f\"beforeSum = {beforeSum}\")
        minValue = sys.maxsize
        for i in range(len(arr)):
            minValue = min(minValue, beforeSum[i] + afterSum[i])
        if (minValue == sys.maxsize):
            minValue = -1
        return minValue

