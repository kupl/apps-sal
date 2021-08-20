class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        res = 0
        A.sort()
        for i in range(len(A)):
            res += 2 ** i * A[i]
            res -= 2 ** (len(A) - 1 - i) * A[i]
        return res % (10 ** 9 + 7)
