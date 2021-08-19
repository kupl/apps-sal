class Solution:
    def distinctSubseqII(self, S: str) -> int:

        # DP(i) = number of distinct subseq ending at i

        # DP(i) = 1 + sum(DP[:i]) if it is a new letter

        # DP(i) = 1 + sum(DP[j:i]) where j is last occurence of letter S[i]

        # abc -> [1, 2, 4]
        # aba -> [1, 2, 3]
        # aaa -> [1, 1, 1]
        # abaa -> [1, 2, 3, 3] a, b, ab, aa, ba, aba, aaa, baa, abaaa

        n = len(S)
        MOD = int(1e9 + 7)
        DP = [0] * n
        I = dict()

        for i, c in enumerate(S):
            if c not in I:
                DP[i] = 1 + sum(DP[:i]) % MOD
            else:
                DP[i] = sum(DP[I[c]:]) % MOD
            I[c] = i

        return sum(DP) % MOD
