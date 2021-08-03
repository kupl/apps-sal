class Solution:
    def distinctSubseqII(self, S: str) -> int:
        MOD = 10**9 + 7
        memo = {}

        def dp(i, j):
            if i > j:
                return 0
            if(i, j) not in memo:
                ans = 1 + dp(i + 1, j) * 2
                for k in range(i + 1, j + 1):
                    if S[k] == S[i]:
                        ans = dp(i + 1, j) * 2 - dp(k + 1, j)
                        break
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, len(S) - 1) % MOD
