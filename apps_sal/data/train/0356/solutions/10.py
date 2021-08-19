class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        if col == 0:
            return False
        (l, r) = (0, row * col - 1)
        while l <= r:
            m = l + r >> 1
            (i, j) = divmod(m, col)
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                r = m - 1
            else:
                l = m + 1
        return False
