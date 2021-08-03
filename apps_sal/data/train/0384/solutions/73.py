class Solution:
    def sumSubseqWidths(self, A: List[int], recursed=False) -> int:
        A.sort()
        return sum(
            x * (2 ** i - 2 ** (len(A) - i - 1)) for i, x in enumerate((A))
        ) % (int(1e9) + 7)
