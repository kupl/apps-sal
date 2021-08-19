class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        A.sort()
        result = 0
        prev = 0
        for i in range(1, len(A)):
            d = A[i] - A[i - 1]
            prev = (2 * prev + d * (pow(2, i, MOD) - 1)) % MOD
            result = (result + prev) % MOD
        return result
