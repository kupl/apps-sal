class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        allowance = K
        currSum = 0
        left = 0
        maxSum = 0
        for i in range(len(A)):
            if A[i] == 1:
                currSum += 1
            else:
                allowance -= 1
                while allowance < 0:
                    if A[left] == 1:
                        currSum -= 1
                    else:
                        allowance += 1
                    left += 1
            maxSum = max(maxSum, K - allowance + currSum)
        return maxSum
