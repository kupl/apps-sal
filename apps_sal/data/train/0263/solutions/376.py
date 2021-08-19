class Solution:

    def __init__(self):
        self.moves = [[4, 6], [8, 6], [7, 9], [4, 8], [9, 3, 0], [], [7, 1, 0], [6, 2], [1, 3], [2, 4]]
        self.memoized_current_number_and_remaining_moves = {}

    def getNextMoves(self, current_number):
        return self.moves[current_number]

    def knightDialer(self, n: int) -> int:
        total_moves = 0
        for number in range(10):
            total_moves += self.knightDialerOneNumber(number, n - 1)
        return total_moves % (pow(10, 9) + 7)

    def knightDialerOneNumber(self, current_number, moves_left):
        if moves_left == 0:
            return 1
        moves = 0
        for move in self.getNextMoves(current_number):
            if (move, moves_left) in list(self.memoized_current_number_and_remaining_moves.keys()):
                moves += self.memoized_current_number_and_remaining_moves[move, moves_left]
            else:
                self.memoized_current_number_and_remaining_moves[move, moves_left] = self.knightDialerOneNumber(move, moves_left - 1)
                moves += self.memoized_current_number_and_remaining_moves[move, moves_left]
        return moves
