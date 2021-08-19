class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        N = len(A)
        A = sorted(A)
        MODS = 10 ** 9 + 7
        (pow2, res) = ([1], 0)
        for ii in range(1, N):
            pow2.append(2 * pow2[-1] % MODS)
        for (ii, jj) in enumerate(A):
            res = (res + (pow2[ii] - pow2[N - ii - 1]) * jj) % MODS
        return res
