class Solution:

    def knightDialer(self, n: int) -> int:
        numMoves = {}
        for i in range(10):
            numMoves[1, i] = 1
        for i in range(2, n + 1):
            numMoves[i, 1] = numMoves[i - 1, 6] + numMoves[i - 1, 8] % (10 ** 9 + 7)
            numMoves[i, 2] = numMoves[i - 1, 7] + numMoves[i - 1, 9] % (10 ** 9 + 7)
            numMoves[i, 3] = numMoves[i - 1, 4] + numMoves[i - 1, 8] % (10 ** 9 + 7)
            numMoves[i, 4] = numMoves[i - 1, 3] + numMoves[i - 1, 9] + numMoves[i - 1, 0] % (10 ** 9 + 7)
            numMoves[i, 5] = 0
            numMoves[i, 6] = numMoves[i - 1, 1] + numMoves[i - 1, 7] + numMoves[i - 1, 0] % (10 ** 9 + 7)
            numMoves[i, 7] = numMoves[i - 1, 2] + numMoves[i - 1, 6] % (10 ** 9 + 7)
            numMoves[i, 8] = numMoves[i - 1, 1] + numMoves[i - 1, 3] % (10 ** 9 + 7)
            numMoves[i, 9] = numMoves[i - 1, 2] + numMoves[i - 1, 4] % (10 ** 9 + 7)
            numMoves[i, 0] = numMoves[i - 1, 4] + numMoves[i - 1, 6] % (10 ** 9 + 7)
        totalMoves = 0
        for i in range(10):
            totalMoves += numMoves[n, i]
        return totalMoves % (10 ** 9 + 7)
