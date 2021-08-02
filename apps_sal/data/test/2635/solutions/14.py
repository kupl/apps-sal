class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        result = []
        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            for i in range(top, bottom):
                result.append(matrix[i][right])
            for i in range(right, left, -1):
                result.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                result.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if left == right and top == bottom:
            result.append(matrix[top][left])
        elif left == right:
            for i in range(top, bottom + 1):
                result.append(matrix[i][left])
        elif top == bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
        return result
