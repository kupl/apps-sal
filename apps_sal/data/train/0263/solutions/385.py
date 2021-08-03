class Solution:
    def knightDialer(self, n: int) -> int:
        if n <= 0:
            return 0
        MOD = 10 ** 9 + 7
        g = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp = [[None] * 10 for _ in range(n + 1)]
        # kd(n,start) = sum(kd(n-1,nxtstart) for nxtstart in g[start]))
        # kd(1,start) = 1

        def kd(n, start):
            if n == 1:
                return 1
            if dp[n][start] is None:
                dp[n][start] = sum([kd(n - 1, nxt) for nxt in g[start]])
            return dp[n][start]
        return sum(kd(n, start) for start in range(10)) % MOD
