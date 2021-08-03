class Solution:

    def knightDialer(self, n: int) -> int:
        mem = [[1] for i in range(10)]
        for i in range(1, n):
            for cell in range(10):
                mem[cell].append(self.knightDialerHelper(i, cell, mem))

        ans = sum([x[n - 1] for x in mem])
        return ans % (10 ** 9 + 7)

    def knightDialerHelper(self, n, cellNumber, mem):

        moves = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        ans = 0
        for nextCell in moves[cellNumber]:
            ans += mem[nextCell][n - 1]
        return ans
