class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        memo = [[0] * (K + 1) for _ in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                memo[m][k] = memo[m - 1][k - 1] + 1 + memo[m - 1][k]
                if memo[m][k] >= N:
                    return m
