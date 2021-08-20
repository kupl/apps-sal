class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        L1 = len(text1)
        L2 = len(text2)
        A = [[0] * (L2 + 1) for i in range(L1 + 1)]
        Max = 0
        for i in range(L1, -1, -1):
            for j in range(L2, -1, -1):
                if i < L1 and j < L2:
                    if text1[i] == text2[j]:
                        A[i][j] = A[i + 1][j + 1] + 1
                    else:
                        A[i][j] = max(A[i][j + 1], A[i + 1][j])
                if Max < A[i][j]:
                    Max = A[i][j]
        return A[i][j]
