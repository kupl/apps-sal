class Solution:
    def knightDialer(self, n: int) -> int:
        a, M = [1] * 10, 10**9 + 7
        moves = [(4, 6), (6, 8), (7, 9), (4, 8), (0, 3, 9), (), (0, 1, 7), (2, 6), (1, 3), (2, 4)]
        for _ in range(1, n):
            b = [0] * 10
            for i in range(10):
                for j in moves[i]:
                    b[i] = (b[i] + a[j]) % M
            a = b

        return sum(a) % M
