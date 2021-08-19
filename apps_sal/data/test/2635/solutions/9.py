class Solution:

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        ans = matrix[0]
        m = len(matrix)
        n = len(matrix[0])
        (row_m, column_m) = (n - 1, m - 1)
        (row_dir, column_dir) = (-1, 1)
        (i0, j0) = (0, n - 1)
        while column_m > 0:
            ans.extend([matrix[i0 + i * column_dir][j0] for i in range(1, column_m + 1)])
            i0 += column_m * column_dir
            column_m -= 1
            column_dir *= -1
            if row_m == 0:
                return ans
            else:
                ans.extend([matrix[i0][j0 + row_dir * i] for i in range(1, row_m + 1)])
                j0 += row_m * row_dir
                row_m -= 1
                row_dir *= -1
        return ans
