class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if L + M == len(A):
            return sum(A)

        prefixSums = [0] * len(A)
        prefixSums[0] = A[0]
        for i in range(1, len(A)):
            prefixSums[i] = prefixSums[i - 1] + A[i]
        # print(prefixSums)

        maxSum = -1
        tempSum = None
        secondTemp = None
        for i in range(0, len(A) - L + 1):
            if i == 0:
                tempSum = prefixSums[i + L - 1]
            else:
                tempSum = prefixSums[i + L - 1] - prefixSums[i - 1]

            for j in range(0, len(A) - M + 1):
                if j + M - 1 < i or j > i + L - 1:
                    if j == 0:
                        secondTemp = prefixSums[j + M - 1]
                    else:
                        secondTemp = prefixSums[j + M - 1] - prefixSums[j - 1]

                    if maxSum < tempSum + secondTemp:
                        maxSum = tempSum + secondTemp

        return maxSum
