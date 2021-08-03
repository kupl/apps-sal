class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        minLen = float('inf')
        lsize = float('inf')
        preSum = {0: -1}
        curSum = 0
        for i, val in enumerate(arr):
            curSum += val
            preSum[curSum] = i
        curSum = 0
        for i, val in enumerate(arr):
            curSum += val
            if curSum - target in preSum:
                lsize = min(lsize, i - preSum[curSum - target])
            if curSum + target in preSum and lsize != float('inf'):
                minLen = min(minLen, preSum[curSum + target] - i + lsize)
        return minLen if minLen != float('inf') else -1
