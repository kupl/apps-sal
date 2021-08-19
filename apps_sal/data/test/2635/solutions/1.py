class Solution:

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        def layer(width, height, top, left):
            if not (width > 0 and height > 0):
                return
            for i in range(left, left + width):
                yield matrix[top][i]
            if height != 1:
                for i in range(top + 1, top + height):
                    yield matrix[i][left + width - 1]
                for i in range(left + width - 2, left - 1, -1):
                    yield matrix[top + height - 1][i]
                if width != 1:
                    for i in range(top + height - 2, top, -1):
                        yield matrix[i][left]
            yield from layer(width - 2, height - 2, top + 1, left + 1)
        return list(layer(len(matrix[0]), len(matrix), 0, 0))
