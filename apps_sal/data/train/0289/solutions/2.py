class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        sub_L = [sum(A[i:i + L]) for i in range(len(A) - L + 1)]
        sub_M = [sum(A[i:i + M]) for i in range(len(A) - M + 1)]

        max_L_M = float('-inf')
        max_M_L = float('-inf')

        p, q = 0, L
        while q < len(sub_M):
            if sub_L[q - L] > sub_L[p]:
                p = q - L
            max_L_M = max(max_L_M, sub_M[q] + sub_L[p])
            q += 1

        q, p = 0, M
        while p < len(sub_L):
            if sub_M[p - M] > sub_M[q]:
                q = p - M
            max_M_L = max(max_M_L, sub_L[p] + sub_M[q])
            p += 1

        return max(max_L_M, max_M_L)
