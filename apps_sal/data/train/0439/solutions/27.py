class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        max_len = 1
        c1 = 1
        c2 = 1
        for i in range(len(A) - 1):
            c1 = c1 + 1 if i % 2 != 0 and A[i] > A[i + 1] or (i % 2 == 0 and A[i] < A[i + 1]) else 1
            c2 = c2 + 1 if i % 2 == 0 and A[i] > A[i + 1] or (i % 2 != 0 and A[i] < A[i + 1]) else 1
            max_len = max(max_len, c1, c2)
        return max_len
