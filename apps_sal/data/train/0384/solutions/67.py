class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        N = len(A)
        return sum((num * (2 ** i - 2 ** (N - i - 1)) for (i, num) in enumerate(A))) % (10 ** 9 + 7)
