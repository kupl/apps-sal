class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        c = 0
        n = len(A)
        for i in range(n):
            c = (2 ** i - 2 ** (n - i - 1)) * A[i] + c
            c = c % (10 ** 9 + 7)
        return c
