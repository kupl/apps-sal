class Solution:

    def __init__(self):
        self.moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [7, 1, 0], [6, 2], [1, 3], [4, 2]]
        self.memoized_moves = {}

    def knightDialer(self, n: int) -> int:
        moves = 0
        for i in range(10):
            moves += self.calculateMoves(n - 1, i)
        return moves % (pow(10, 9) + 7)

    def calculateMoves(self, moves_remaining, current_number):
        if moves_remaining == 0:
            return 1
        moves = 0
        for next_number in self.getMoves(current_number):
            if (moves_remaining, next_number) not in self.memoized_moves:
                self.memoized_moves[moves_remaining, next_number] = self.calculateMoves(moves_remaining - 1, next_number)
            moves += self.memoized_moves[moves_remaining, next_number]
        return moves

    def getMoves(self, number):
        return self.moves[number]
