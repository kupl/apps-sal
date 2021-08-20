class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        (L, M) = (min(L, M), max(L, M))
        lSums = [0] * len(A)
        mSums = [0] * len(A)
        lSums[L - 1] = sum(A[:L])
        mSums[M - 1] = sum(A[:M])
        for i in range(L, len(A)):
            lSums[i] = lSums[i - 1] + A[i] - A[i - L]
        for i in range(M, len(A)):
            mSums[i] = mSums[i - 1] + A[i] - A[i - M]
        print(lSums)
        print(mSums)
        greatest = 0
        for i in range(L - 1, len(A) - M):
            greatest = max(greatest, max(lSums[:i + 1]) + max(mSums[i + M:]))
        for i in range(M - 1, len(A) - L):
            greatest = max(greatest, max(mSums[:i + 1]) + max(lSums[i + L:]))
        return greatest
