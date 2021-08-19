class Solution:

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        v = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        res = []
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        dest = m * n
        way = 0
        offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while count < dest:
            res.append(matrix[i][j])
            count += 1
            v[i][j] = True
            if not 0 <= i + offset[way][0] < m or not 0 <= j + offset[way][1] < n or v[i + offset[way][0]][j + offset[way][1]]:
                way = (way + 1) % 4
            i += offset[way][0]
            j += offset[way][1]
        return res
