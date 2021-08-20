class Solution:

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        level = 0
        r = []
        while len(r) < len(matrix) * len(matrix[0]):
            if level % 4 == 0:
                r += matrix[level // 4][level // 4:len(matrix[0]) - level // 4]
            elif level % 4 == 1:
                side_index = len(matrix[0]) - level // 4 - 1
                for i in range(level // 4 + 1, len(matrix) - level // 4):
                    r.append(matrix[i][side_index])
            elif level % 4 == 2:
                r += matrix[len(matrix) - 1 - level // 4][level // 4:len(matrix[0]) - level // 4 - 1][::-1]
            elif level % 4 == 3:
                side_index = level // 4
                for i in range(len(matrix) - 1 - level // 4 - 1, level // 4, -1):
                    r.append(matrix[i][side_index])
            level += 1
        return r
