class Solution:

    def __init__(self):
        self.moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [7, 1, 0], [6, 2], [1, 3], [4, 2]]
        self.memoized_numbers = {}

    def knightDialer(self, n: int) -> int:
        distinctPhoneNumbers = 0
        for i in range(10):
            distinctPhoneNumbers += self.getPhoneNumbers(n - 1, i)
        return distinctPhoneNumbers % (pow(10, 9) + 7)

    def getPhoneNumbers(self, moves_remaining, current_number):
        if moves_remaining == 0:
            return 1
        else:
            moves = 0
            for number in self.getMoves(current_number):
                if (moves_remaining, number) not in list(self.memoized_numbers.keys()):
                    self.memoized_numbers[moves_remaining, number] = self.getPhoneNumbers(moves_remaining - 1, number)
                moves += self.memoized_numbers[moves_remaining, number]
            return moves

    def getMoves(self, move):
        return self.moves[move]
