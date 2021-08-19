from collections import defaultdict


class Solution:

    def getSubArray(self, array, target):
        dic = defaultdict(int)
        minSub = [float('inf')] * len(array)
        currentSum = 0
        for (i, num) in enumerate(array):
            currentSum += num
            if currentSum == target:
                minSub[i] = i - 0 + 1
            elif currentSum - target in dic:
                minSub[i] = i - dic[currentSum - target] + 1
            minSub[i] = min(minSub[i - 1], minSub[i])
            dic[currentSum] = i + 1
        return minSub

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        result = float('inf')
        leftMinSub = self.getSubArray(arr, target)
        rightMinSub = self.getSubArray(arr[::-1], target)[::-1]
        for i in range(1, n):
            result = min(result, leftMinSub[i - 1] + rightMinSub[i])
        if result == float('inf'):
            return -1
        else:
            return result
