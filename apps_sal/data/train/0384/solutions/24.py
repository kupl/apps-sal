class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        return sum((1 << i) * num - (1 << len(A) - i - 1) * num for i, num in enumerate(sorted(A))) % (10**9 + 7)
