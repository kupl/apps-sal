class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output_arr = []

        while matrix:

            output_arr.extend(matrix.pop(0))

            tmp_arr = []
            for i in zip(*matrix):
                tmp_arr.append(list(i))

            matrix = tmp_arr[::-1]

        return output_arr
