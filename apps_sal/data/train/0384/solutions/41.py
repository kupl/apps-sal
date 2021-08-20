class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A = sorted(A)
        (total, cur, cnt) = (0, 0, 0)
        MOD = 10 ** 9 + 7
        for i in range(1, len(A)):
            cnt *= 2
            cnt += 1
            cur *= 2
            cur += (A[i] - A[i - 1]) * cnt
            cur %= MOD
            total += cur
            total %= MOD
        return total
