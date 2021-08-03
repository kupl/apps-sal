class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        POW2 = [(1 << i) % MOD for i in range(len(A))]
        return sum((POW2[i] - POW2[len(A) - 1 - i]) * n for i, n in enumerate(sorted(A))) % (10 ** 9 + 7)
