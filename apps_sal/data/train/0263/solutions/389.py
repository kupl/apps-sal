class Solution:
    def pos(self, idx):
        return {0: [4, 6],
                1: [6, 8],
                2: [9, 7],
                3: [4, 8],
                4: [3, 9, 0],
                5: [],
                6: [1, 7, 0],
                7: [6, 2],
                8: [1, 3],
                9: [4, 2]}[idx]

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        memo = [[0 for _ in range(n + 1)] for i in range(10)]
        for i in range(10):
            memo[i][1] = 1
        for s in range(2, n + 1):
            for idx in range(10):
                for p in self.pos(idx):
                    memo[idx][s] += memo[p][s - 1]
        return sum((memo[i][n] for i in range(10))) % (10 ** 9 + 7)


