class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        currMaxSum = 0
        currMinSum = 0
        flag = False
        maxSum = float('-inf')
        minSum = float('inf')
        totalSum = 0
        for i in range(len(A)):
            currMaxSum += A[i]
            maxSum = max(maxSum, currMaxSum)
            if currMaxSum < 0:
                currMaxSum = 0
            totalSum += A[i]
            if A[i] >= 0:
                flag = True
            currMinSum += A[i]
            minSum = min(minSum, currMinSum)
            if currMinSum > 0:
                currMinSum = 0
        if not flag:
            return maxSum
        else:
            return max(maxSum, totalSum - minSum)
