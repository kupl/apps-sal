class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        N = len(A)
        i = 0
        max_l = 1

        for j in range(1, N):
            if A[j - 1] == A[j]:
                i = j
            elif (j == N - 1) or ((A[j - 1] < A[j]) ^ (A[j] > A[j + 1])) or ((A[j - 1] == A[j]) or (A[j] == A[j + 1])):
                max_l = max(max_l, j - i + 1)
                i = j

        return max_l
