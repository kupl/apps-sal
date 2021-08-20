class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        result = 0
        lsum = sum(A[0:L])
        msum = sum(A[L:L + M])
        psum = 0
        j = 0
        result = max(result, max(lsum + msum, lsum + psum))
        prefix = [0] * len(A)
        for i in range(0, len(A) - M + 1):
            prefix[i + M - 1] = sum(A[i:i + M])
        for k in range(L + M - 1, len(A)):
            result = max(result, lsum + prefix[k])
        for i in range(L, len(A)):
            lsum = lsum - A[i - L] + A[i]
            if i + M <= len(A) - 1:
                for k in range(i + M, len(A)):
                    result = max(result, lsum + prefix[k])
            if i - L > M - 1:
                for k in range(0, i - L):
                    result = max(result, lsum + prefix[k])
        return result
