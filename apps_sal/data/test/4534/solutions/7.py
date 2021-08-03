class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rows = [1]
        for i in range(rowIndex):
            rows = [x + y for x, y in zip([0] + rows, rows + [0])]
        return rows
