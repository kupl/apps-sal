class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        return sum(((1 << i) - (1 << (len(A) - 1 - i))) * n for i, n in enumerate(sorted(A))) % (10 ** 9 + 7)

