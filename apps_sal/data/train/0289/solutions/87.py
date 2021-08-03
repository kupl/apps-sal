class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        lhash, mhash = dict(), dict()
        for i in range(len(A) - L + 1):
            if i == 0:
                lhash[i] = sum(A[:L])
            else:
                lhash[i] = lhash[i - 1] - A[i - 1] + A[i + L - 1]

        for i in range(len(A) - M + 1):
            if i == 0:
                mhash[i] = sum(A[:M])
            else:
                mhash[i] = mhash[i - 1] - A[i - 1] + A[i + M - 1]

        res = 0
        for i in range(0, len(A) - L + 1):
            if i > len(A) - M:
                break
            for j in range(i + L - 1 + 1, len(A) - M + 1):
                res = max(res, lhash[i] + mhash[j])

        for j in range(0, len(A) - M + 1):
            if j > len(A) - L:
                break

            for i in range(j + M - 1 + 1, len(A) - L + 1):
                res = max(res, lhash[i] + mhash[j])

        return res
