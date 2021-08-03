class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N = len(A)

        res = 0
        for i in range(N - L + 1):
            l_sum = sum(A[i:i + L])
            for j in list(range(i - M + 1)) + list(range(i + L, N - M + 1)):
                res = max(res, l_sum + sum(A[j:j + M]))
        return res
