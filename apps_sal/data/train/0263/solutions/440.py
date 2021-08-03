class Solution:
    def __init__(self):
        self.moves = [
            [4, 6],
            [8, 6],
            [7, 9],
            [4, 8],
            [9, 3, 0],
            [],
            [7, 1, 0],
            [6, 2],
            [1, 3],
            [2, 4],
        ]

        self.memoized_results = {}

    def knightDialer(self, n: int) -> int:
        total_moves = 0
        for number in range(10):
            moves = self.knightDialerOnOneDigit(number, n - 1)
            total_moves += moves
        return(total_moves % (pow(10, 9) + 7))

    def knightDialerOnOneDigit(self, current_number, remaining_moves):
        if remaining_moves == 0:
            return 1

        moves = 0
        for number in self.moves[current_number]:
            if (number, remaining_moves - 1) in list(self.memoized_results.keys()):
                new_moves = self.memoized_results[(number, remaining_moves - 1)]
            else:
                new_moves = self.knightDialerOnOneDigit(number, remaining_moves - 1)
                self.memoized_results[(number, remaining_moves - 1)] = new_moves
            moves += new_moves
        return moves
