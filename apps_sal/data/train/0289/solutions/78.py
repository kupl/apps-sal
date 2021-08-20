class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        sum = [0 for i in range(len(A))]
        sum[0] = A[0]
        for i in range(1, len(A)):
            sum[i] = sum[i - 1] + A[i]
        res = -math.inf
        for i in range(len(A) - L):
            r = -math.inf
            for j in range(i + L, len(A) - M + 1):
                r = max(r, sum[j + M - 1] - sum[j - 1])
            r += sum[i + L - 1] - (sum[i - 1] if i - 1 > -1 else 0)
            res = max(res, r)
        for i in range(len(A) - M):
            r = -math.inf
            for j in range(i + M, len(A) - L + 1):
                r = max(r, sum[j + L - 1] - sum[j - 1])
            r += sum[i + M - 1] - (sum[i - 1] if i - 1 > -1 else 0)
            res = max(res, r)
        return res
