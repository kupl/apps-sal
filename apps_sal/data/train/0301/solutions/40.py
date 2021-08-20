class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if len(A) == 0 or len(B) == 0:
            return 0
        A = [-1] + A
        B = [-1] + B
        res = [[0 for _ in range(len(B))] for _ in range(len(A))]
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    res[i][j] = res[i - 1][j - 1] + 1
                else:
                    res[i][j] = max(res[i - 1][j], res[i][j - 1])
        return res[-1][-1]
