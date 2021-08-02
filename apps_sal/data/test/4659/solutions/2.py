class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            newRow = [1]
            for j in range(1, i):
                newRow.append(res[-1][j - 1] + res[-1][j])
            newRow.append(1)
            res.append(newRow)
        return res
