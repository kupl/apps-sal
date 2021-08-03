class Solution:
    def knightDialer(self, n: int) -> int:
        adj = [
            [4, 6],
            [8, 6],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        m = 10 ** 9 + 7

        memo = [1] * 10
        for i in range(1, n):
            memo = [sum(memo[e] for e in adj[d]) % m for d in range(10)]

        return sum(memo) % m
