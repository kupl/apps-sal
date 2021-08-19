class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if not A:
            return 0
        cumulatedSum = [0] * (len(A) + 1)
        result = 0
        for i in range(len(A)):
            cumulatedSum[i + 1] = cumulatedSum[i] + A[i]
        for i in range(len(A) - L + 1):
            lSum = cumulatedSum[i + L] - cumulatedSum[i]
            for j in range(i + L, len(A) - M + 1):
                mSum = cumulatedSum[j + M] - cumulatedSum[j]
                result = max(result, lSum + mSum)
        for i in range(len(A) - M + 1):
            mSum = cumulatedSum[i + M] - cumulatedSum[i]
            for j in range(i + M, len(A) - L + 1):
                lSum = cumulatedSum[j + L] - cumulatedSum[j]
                result = max(result, lSum + mSum)
        return result
