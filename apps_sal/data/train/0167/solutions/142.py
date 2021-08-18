class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        drops = 0
        floors = [0] * (K + 1)
        while floors[K] < N:
            for eggs in range(K, 0, -1):
                floors[eggs] += 1 + floors[eggs - 1]
            drops += 1
        return drops

    def superEggDrop(self, K: int, N: int) -> int:
        M = N
        dp = [[0 for j in range(K + 1)] for i in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, K + 1):
                dp[i][j] = 1 + dp[i - 1][j] + dp[i - 1][j - 1]
                if dp[i][j] >= N:
                    return i
