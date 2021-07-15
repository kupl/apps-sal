class Solution:
    def minDeletionSize(self, A):
        m, n = len(A), len(A[0])
        first = [False] * m
        res = 0
        for j in range(n):
            for i in range(1, m):
                if not first[i] and A[i][j] < A[i - 1][j]:
                    res += 1
                    break
            else:
                for i in range(1, m):
                    if A[i][j] > A[i - 1][j]:
                        first[i] = True
        return res        
