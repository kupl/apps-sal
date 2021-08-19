class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        total = 0
        for (i, a) in enumerate(A):
            left = i
            right = n - i - 1
            total += (2 ** left - 1) * a
            total -= (2 ** right - 1) * a
        return total % (10 ** 9 + 7)
