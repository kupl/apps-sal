from collections import defaultdict


class Solution:
    def knightDialer(self, n: int) -> int:
        self.buildPad()
        self.buildMoves()

        self.memo = [[-1 for _ in range(n)] for _ in range(10)]

        numbers = sum(self.visit(start, n - 1) for start in range(10))

        return numbers % (10**9 + 7)

    def visit(self, start: int, n: int) -> int:
        if n == 0:
            return 1
        elif self.memo[start][n] != -1:
            return self.memo[start][n]

        numbers = 0
        for new_start in self.moves[start]:
            numbers += self.visit(new_start, n - 1)

        self.memo[start][n] = numbers
        return numbers

    def buildPad(self) -> None:
        self.pad = [[str(i + j) for j in range(3)] for i in range(1, 10, 3)]
        self.pad.append(['*', '0', '

    def buildMoves(self) -> None:
        self.moves=(
            (4, 6),
            (6, 8),
            (7, 9),
            (4, 8),
            (0, 3, 9),
            (),
            (0, 1, 7),
            (2, 6),
            (1, 3),
            (2, 4)
        )
