class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        mat = [[0] * (len(B) + 1) for j in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    mat[i][j] = mat[i - 1][j - 1] + 1
                else:
                    mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])
        return mat[-1][-1]
