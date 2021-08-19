class Solution:

    def superEggDrop(self, K: int, N: int) -> int:

        def dp(m, k):
            if m <= 1 or k == 1:
                return m
            if (m, k) in memo:
                return memo[m, k]
            memo[m, k] = dp(m - 1, k - 1) + 1 + dp(m - 1, k)
            return memo[m, k]
        memo = {}
        for i in range(N + 1):
            if dp(i, K) >= N:
                return i
