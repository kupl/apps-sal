class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        res = []
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = col - 1
        down = row - 1
        up = 0
        direction = 0
        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for i in reversed(range(left, right + 1)):
                    res.append(matrix[down][i])
                down -= 1
            if direction == 3:
                for i in reversed(range(up, down + 1)):
                    res.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
            if left > right or up > down:
                return res
