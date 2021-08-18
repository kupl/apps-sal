from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        return self.findMoves(K, N)

    @lru_cache(maxsize=None)
    def findMoves(self, K, N):
        if K == 1 or N <= 1:
            return N
        f = N

        left, right = 1, N
        while (left < right):
            mid = (left + right) // 2

            broken = self.findMoves(K - 1, mid - 1)
            intact = self.findMoves(K, N - mid)
            if broken > intact:
                right = mid
            else:
                left = mid + 1

        mid = left - 1
        return 1 + max(self.findMoves(K - 1, mid - 1), self.findMoves(K, N - mid))

    def bottomUp(self, K, N):
        dp = [[i for i in range(N + 1)] for _ in range(K + 1)]
        for i in range(2, K + 1):
            for j in range(1, N + 1):
                min_drops = N
                for k in range(1, j + 1):
                    min_drops = min(min_drops, 1 + max(dp[i - 1][k - 1], dp[i][j - k]))
                dp[i][j] = min_drops
        return dp[K][N]
