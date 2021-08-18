class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        preSum = {0: -1}
        n = len(arr)
        curSum = 0
        minLen = float('inf')
        lsize = float('inf')
        for i in range(n):
            curSum += arr[i]
            preSum[curSum] = i
        curSum = 0
        for i in range(n):
            curSum += arr[i]
            if curSum - target in preSum:
                lsize = min(lsize, i - preSum[curSum - target])
            if curSum + target in preSum and lsize != float('inf'):
                minLen = min(minLen, preSum[curSum + target] - i + lsize)
        return minLen if minLen != float('inf') else -1
