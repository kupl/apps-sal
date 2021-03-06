class Solution:

    def countOrders(self, n: int) -> int:
        MOD = int(1000000000.0) + 7
        d = [[0] * (n + 2) for _ in range(n + 2)]
        d[0][0] = 1
        for i in range(n + 1):
            for j in range(i + 1):
                d[i + 1][j] = (d[i + 1][j] + d[i][j] * (n - i)) % MOD
                d[i][j + 1] = (d[i][j + 1] + d[i][j] * (i - j)) % MOD
        return d[n][n - 1]
