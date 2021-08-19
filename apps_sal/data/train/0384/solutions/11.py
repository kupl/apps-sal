class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        res = 0
        n = len(A)
        M = 10**9 + 7
        c = 1
        A.sort()

        for i in range(n):
            res = (res + A[i] * c - A[n - i - 1] * c) % M
            # print(res)
            c = (c << 1) % M
        return res
