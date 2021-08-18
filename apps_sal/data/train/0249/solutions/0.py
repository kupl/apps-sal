class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        magic_squares = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                window = [tmp[j:j + 3] for tmp in grid[i: i + 3]]
                if self.isMagicSquare(window):
                    magic_squares += 1

        return magic_squares

    def isMagicSquare(self, square: List[List[int]]) -> bool:
        target = square[0][0] + square[0][1] + square[0][2]
        seen = {}
        print(square)
        for row in square:
            tmp = 0
            for i in row:
                tmp += i
                if i in seen or i > 9 or i < 1:
                    return False
                else:
                    seen[i] = 1
            if tmp != target:
                return False

        for i in range(3):
            tmp = 0
            for row in square:
                tmp += row[i]

            if tmp != target:
                return False

        tmp = 0
        for i in range(3):
            tmp += square[i][i]
        if tmp != target:
            return False

        tmp = 0
        for i in range(3):
            tmp += square[i][2 - i]
        if tmp != target:
            return False

        return True
