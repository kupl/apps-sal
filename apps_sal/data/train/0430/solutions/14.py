class Solution:

    def distinctSubseqII(self, S: str) -> int:
        n = len(S)
        MOD = int(1000000000.0 + 7)
        DP = [0] * n
        I = dict()
        for (i, c) in enumerate(S):
            if c not in I:
                DP[i] = 1 + sum(DP[:i]) % MOD
            else:
                DP[i] = sum(DP[I[c]:]) % MOD
            I[c] = i
        return sum(DP) % MOD
