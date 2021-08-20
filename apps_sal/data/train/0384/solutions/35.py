class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        total = 0
        for i in range(n):
            a = A[i]
            left = i
            right = n - i - 1
            total += ((1 << left) - 1) * a
            total -= ((1 << right) - 1) * a
        return total % (10 ** 9 + 7)
