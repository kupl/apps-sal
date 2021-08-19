class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        result = 0
        for i in range(len(A)):
            result *= 2
            result -= A[i]
            result += A[~i]
        return result % (10 ** 9 + 7)
