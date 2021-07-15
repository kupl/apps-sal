class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # PreSum. for every i, find the minimum value of length of sub-array on the left or starting with i whose value is equal to target. Find another sub-array starting with i+1, whose sum is target. Update the result with the minimum value of the sum of both the sub-array. This is possible because all values are positive and the value of sum is strictly increasing, meaning arr[i]+target will always be on the right of i, and, if arr[i]+target exists, there will only be one answer (this condition also applies to arr[i]-target, there will only be one answer for each i if the answer exists, as the array is strictly increasing and there's no zeros) 
        
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
            if curSum-target in preSum:
                lsize = min(lsize, i-preSum[curSum-target])
            if curSum+target in preSum and lsize != float('inf'):
                minLen = min(minLen, preSum[curSum+target]-i+lsize)
        return minLen if minLen != float('inf') else -1

