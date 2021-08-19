class Solution:

    def distinctSubseqII(self, S: str) -> int:
        n = len(S)
        MOD = int(1000000000.0 + 7)
        I = dict()
        PS = [0] * (n + 1)
        for (i, c) in enumerate(S):
            if c not in I:
                dpi = 1 + PS[i] % MOD
            else:
                dpi = PS[i] - PS[I[c]]
            I[c] = i
            PS[i + 1] = PS[i] + dpi
        return PS[-1] % MOD
