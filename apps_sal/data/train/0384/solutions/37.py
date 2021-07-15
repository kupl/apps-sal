class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A = sorted(A)
        r = 0
        m = 10 ** 9 + 7
        for i in range(len(A)-1):
            # print(r)
            # print(A[i+1] - A[i], len(A)-i)
            r += (A[i+1] - A[i]) * ((1 << (len(A))) - (1 << (i+1)) - (1 << (len(A)-i-1)) + 1)
        r %= m
        return r
