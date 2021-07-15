class Solution:
    def sumSubseqWidths(self, A: List[int], recursed=False) -> int:
        return sum(
            x * (2 ** i - 2 ** (len(A) - i - 1)) for i, x in enumerate(sorted(A))
        ) % (int(1e9) + 7)

