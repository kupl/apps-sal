class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        dp = dict()
        for i in A:
            dp[(i, i)] = 0

        n = len(A)

        for i in range(n):
            for j in range(i + 1, n):

                if A[j] - A[i] < A[i] and A[j] - A[i] >= 0 and (A[j] - A[i], A[i]) in dp:
                    val = dp[(A[j] - A[i], A[i])] + 1
                else:
                    val = 2
                dp[(A[i], A[j])] = val
        a = max(list(dp.values()))
        if a > 2:
            return a
        return 0
