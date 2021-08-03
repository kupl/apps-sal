class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        total = 0
        const = 10**9 + 7
        for i in range(len(A)):
            total += 2**(i) * A[i] - 2**(len(A) - i - 1) * A[i]
            total = total % const
        return total
