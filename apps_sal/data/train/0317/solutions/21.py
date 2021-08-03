from functools import lru_cache


class Solution:
    def numPermsDISequence(self, S: str) -> int:
        # Dynamic Programming
        # Time  complexity: O(N^3)
        # Space complexity: O(N^2)
        MOD = 10**9 + 7
        N = len(S)

        @lru_cache(None)
        def dp(i, j):
            # How many ways to place P_i with relative rank j?
            if i == 0:
                return 1
            elif S[i - 1] == 'D':
                return sum(dp(i - 1, k) for k in range(j, i)) % MOD
            else:
                return sum(dp(i - 1, k) for k in range(j))

        return sum(dp(N, j) for j in range(N + 1)) % MOD
