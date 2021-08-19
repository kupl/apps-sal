class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if len(A) < M + L:
            return -1

        def getSumM(start, end):
            if end - start < M:
                return 0
            preSumM = sum(A[start:start + M])
            maxM = preSumM
            for i in range(start + 1, end - M + 1):
                preSumM = preSumM - A[i - 1] + A[i + M - 1]
                maxM = max(maxM, preSumM)
            return maxM
        preSumL = sum(A[:L - 1])
        maxSum = -sys.maxsize
        for i in range(len(A) - L + 1):
            preSumL = preSumL + A[i + L - 1]
            leftSumM = getSumM(0, i)
            rightSumM = getSumM(i + L, len(A))
            maxSum = max(maxSum, preSumL + max(leftSumM, rightSumM))
            preSumL = preSumL - A[i]
        return maxSum
