class Solution:

    def minDeletionSize(self, A):
        (m, n) = (len(A), len(A[0]))
        first = [-1] * m
        res = 0
        for j in range(n):
            for i in range(1, m):
                if first[i] == -1 and A[i][j] < A[i - 1][j]:
                    res += 1
                    break
            else:
                for i in range(1, m):
                    if A[i][j] > A[i - 1][j] and first[i] == -1:
                        first[i] = j
        return res
