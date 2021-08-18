class Solution:
    def knightDialer(self, n: int) -> int:

        self.moves = [(4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]
        return sum(self.knightDialer_(n, i) for i in range(10)) % (10**9 + 7)

    def knightDialer_(self, N, i, dp={}):
        if N == 1:
            return 1
        if (N, i) not in dp:
            dp[(N, i)] = sum(self.knightDialer_(N - 1, j) for j in self.moves[i])
        return dp[(N, i)]
