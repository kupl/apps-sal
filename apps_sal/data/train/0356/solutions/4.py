class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        column = len(matrix[0])
        if column == 0:
            return False
        i = 0
        while i < row:
            if target <= matrix[i][column - 1]:
                for j in range(column - 1, -1, -1):
                    if matrix[i][j] == target:
                        return True
                    else:
                        pass
                return False
            else:
                i += 1
        return False
