class Solution:
    def knightDialer(self, n: int) -> int:

        moves = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
                 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        mem = [[0 for i in range(n)] for i in range(10)]

        for i in range(10):
            mem[i][0] = 1

        for col in range(1, n):
            for row in range(10):
                for move in moves[row]:
                    mem[row][col] += mem[move][col - 1]
                    mem[row][col] %= (10**9) + 7

        tot_sum = 0
        for row in range(10):
            tot_sum += mem[row][n - 1]
            tot_sum %= (10**9) + 7

        return tot_sum
