class Solution:
    def knightDialer(self, n: int) -> int:
        adj = {}
        adj[0] = [4, 6]
        adj[1] = [6, 8]
        adj[2] = [7, 9]
        adj[3] = [4, 8]
        adj[4] = [0, 3, 9]
        adj[5] = []
        adj[6] = [0, 1, 7]
        adj[7] = [2, 6]
        adj[8] = [1, 3]
        adj[9] = [2, 4]

        p = 10**9 + 7
        f = [None] * n
        f[0] = [1] * 10
        for i in range(1, n):
            f[i] = [0] * 10
            for v in range(0, 10):
                for u in adj[v]:
                    f[i][v] += f[i - 1][u]

        total = 0
        for d in range(0, 10):
            total = (total % p + f[n - 1][d] % p) % p
        return total
