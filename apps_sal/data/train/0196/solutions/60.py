class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        maxSum = -float('inf')
        currSum = 0
        for j in range(n):
            ele = A[j]
            newSum = currSum + ele
            maxSum = max(maxSum, newSum)
            if currSum > 0 and newSum < 0:
                currSum = 0
            elif currSum <= 0 and newSum < currSum:
                currSum = 0
            else:
                currSum = newSum
        lSum = 0
        bestLSum = 0
        totalSum = sum(A)
        for i in range(n):
            currSum = totalSum - lSum
            currSum += bestLSum
            maxSum = max(maxSum, currSum)
            lSum += A[i]
            bestLSum = max(lSum, bestLSum)
        return maxSum
