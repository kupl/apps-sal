class Solution:

    def minSwap(self, A: List[int], B: List[int]) -> int:
        (no, yes, n) = (0, 1, len(A))
        for i in range(1, n):
            (no_u, yes_u) = (n, n)
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                (no_u, yes_u) = (no, yes + 1)
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                no_u = min(no_u, yes)
                yes_u = min(yes_u, no + 1)
            (no, yes) = (no_u, yes_u)
        return min(no, yes)
