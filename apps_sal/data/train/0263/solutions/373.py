from collections import defaultdict


class Solution:
    def knightDialer(self, N: int) -> int:

        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]

        dp = defaultdict(int)
        movesC = {}

        def moves(i, j):
            valids = set()
            for u, v in [(i - 1, j + 2), (i + 1, j + 2), (i - 1, j - 2), (i + 1, j - 2), (i - 2, j + 1), (i - 2, j - 1), (i + 2, j + 1), (i + 2, j - 1)]:
                if u < 0 or v < 0 or u >= len(board) or v >= 3:
                    continue
                if board[u][v] != -1:
                    valids.add((u, v))
            return valids
        for i in range(len(board)):
            for j in range(3):
                if board[i][j] != -1:
                    movesC[(i, j)] = moves(i, j)
        total = 0
        for n in range(1, N + 1):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    num = board[i][j]
                    if num != -1:
                        key = (i, j, n)
                        if n == 1:
                            dp[key] = 1
                        else:

                            for u, v in movesC[(i, j)]:
                                dp[key] += dp[(u, v, n - 1)]
                        if n == N:
                            total += dp[key]

        return total % (10 ** 9 + 7)
