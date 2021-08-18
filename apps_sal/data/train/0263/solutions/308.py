class Solution:
    def knightDialer(self, n: int) -> int:
        self.edges = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [9, 3, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        self.MAX = (10 ** 9) + 7

        self.ledger = [[None] * n for _ in range(10)]

        dialable = 0
        for cell in range(10):
            dialable += self.knight_dialer(n - 1, cell)

        return dialable % self.MAX

    def knight_dialer(self, steps_left: int, position: int) -> None:
        if not steps_left:
            return 1

        if self.ledger[position][steps_left]:
            return self.ledger[position][steps_left]

        dialable = 0
        for nbr in self.edges[position]:
            dialable += self.knight_dialer(steps_left - 1, nbr) % self.MAX

        self.ledger[position][steps_left] = dialable

        return dialable % (10 ** 9 + 7)
