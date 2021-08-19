class Solution:

    def numPermsDISequence(self, S: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(S)

        @lru_cache(None)
        def dp(i, j):
            if not 0 <= j <= i:
                return 0
            if i == 0:
                return 1
            elif S[i - 1] == 'D':
                return (dp(i, j + 1) + dp(i - 1, j)) % MOD
            else:
                return (dp(i, j - 1) + dp(i - 1, j - 1)) % MOD
        return sum((dp(n, j) for j in range(n + 1))) % MOD
