class Solution:

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        arr = [a for a in range(1, n * n + 1)]
        matrix = [[a for a in range(1, n + 1)] for b in range(1, n + 1)]
        num = 0
        row_s = 0
        row_e = n - 1
        col_s = 0
        col_e = n - 1
        while col_e > col_s and row_e > row_s:
            for i in range(col_s, col_e):
                matrix[row_s][i] = arr[num]
                num += 1
            for i in range(row_s, row_e):
                matrix[i][col_e] = arr[num]
                num += 1
            for i in range(col_e, col_s, -1):
                matrix[row_e][i] = arr[num]
                num += 1
            for i in range(row_e, row_s, -1):
                matrix[i][col_s] = arr[num]
                num += 1
            row_s += 1
            col_s += 1
            row_e -= 1
            col_e -= 1
        if col_s == col_e:
            for i in range(row_s, row_e + 1):
                matrix[i][col_e] = arr[num]
                num += 1
        else:
            for i in range(col_s, col_e + 1):
                matrix[row_s][i] = arr[num]
                num += 1
        return matrix
