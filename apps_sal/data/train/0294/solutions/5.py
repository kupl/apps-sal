class Solution:
    def __init__(self):
        self.board = []
        self.col_status = []
        self.row_status = []
        self.dia_status_1 = []
        self.dia_status_2 = []
        self.result = 0

    def placeQueen(self, row, n):
        if row == n:
            tmp = [''.join(el) for el in self.board]
            self.result += 1
            return
        for i in range(n):
            if self.col_status[i] and self.dia_status_1[i + row] and self.dia_status_2[row - i]:
                self.board[row][i] = 'Q'
                self.col_status[i] = False
                self.dia_status_1[i + row] = False
                self.dia_status_2[row - i] = False
                self.placeQueen(row + 1, n)
                self.board[row][i] = '.'
                self.col_status[i] = True
                self.dia_status_1[i + row] = True
                self.dia_status_2[row - i] = True

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.board = [['.' for i in range(n)] for j in range(n)]
        self.col_status = [True for i in range(n)]
        self.row_status = [True for i in range(n)]
        self.dia_status_1 = [True for i in range(2 * n - 1)]
        self.dia_status_2 = [True for i in range(2 * n - 1)]
        self.placeQueen(0, n)
        return self.result
