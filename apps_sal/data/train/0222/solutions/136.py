class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        L = len(A)
        if L <= 2:
            return 0

        res = dict()
        for j in range(1, L):
            res[A[0], A[j]] = 2
            for i in range(1, j):
                if (A[j] - A[i], A[i]) in res:
                    res[A[i], A[j]] = max(res.get((A[i], A[j]), 2), res[A[j] - A[i], A[i]] + 1)
                else:
                    res[A[i], A[j]] = 2
        maxx = max(list(res.values()))
        if maxx >= 3:
            return maxx
        else:
            return 0
