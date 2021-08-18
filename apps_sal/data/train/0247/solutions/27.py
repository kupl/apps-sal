class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        result = float('inf')
        leftmin = self.getMinLen(arr, target, True)
        rightmin = self.getMinLen(arr, target, False)
        for i in range(0, len(arr) - 1):
            result = min(result, leftmin[i] + rightmin[i + 1])
        return result if result != float('inf') else -1

    def getMinLen(self, arr, target, l2r):
        if not l2r:
            arr = arr[::-1]
        memo = {0: 0}
        result = [float('inf')] * len(arr)
        curSum = 0
        for i, num in enumerate(arr):
            if i > 0:
                result[i] = result[i - 1]
            curSum += num
            if curSum - target in memo:
                curLen = i - memo[curSum - target] + 1
                result[i] = min(result[i], curLen)
            memo[curSum] = i + 1
        if not l2r:
            result = result[::-1]
        return result
