class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        largestSum = 0
        (LList, MList) = ([0] * len(A), [0] * len(A))
        thisSum = sum(A[:L])
        LList[0] = thisSum
        for idx in range(len(A) - L):
            thisSum += A[idx + L] - A[idx]
            LList[idx + 1] = thisSum
        thisSum = sum(A[:M])
        MList[0] = thisSum
        for idx in range(len(A) - M):
            thisSum += A[idx + M] - A[idx]
            MList[idx + 1] = thisSum
        for idx in range(len(A) - M + 1):
            largestSum = max(largestSum, MList[idx] + max([0] + LList[:max(0, idx - L + 1)] + LList[idx + M:]))
        return largestSum
