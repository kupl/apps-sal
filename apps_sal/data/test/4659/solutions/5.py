class Solution:

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        base = [1]
        triangle = [base]
        for i in range(1, numRows):
            new_row = [1]
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            new_row.append(1)
            triangle.append(new_row)
        return triangle
