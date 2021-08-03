class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if((len_A := len(A)) == 0 or (len_B := len(B)) == 0):
            return 0
        matrix = [[0 for i in range(len_B + 1)] for k in range(len_A + 1)]
        for i in range(1, len_A + 1):
            for k in range(1, len_B + 1):
                if(A[i - 1] == B[k - 1]):
                    matrix[i][k] = matrix[i - 1][k - 1] + 1
                else:
                    matrix[i][k] = max(matrix[i - 1][k - 1], matrix[i - 1][k], matrix[i][k - 1])
        return matrix[-1][-1]
