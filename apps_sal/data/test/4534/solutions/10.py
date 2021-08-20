class Solution:

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        i = 1
        res = [1]
        while rowIndex >= 1:
            res.append(int(res[-1] * rowIndex / i))
            (rowIndex, i) = (rowIndex - 1, i + 1)
        return res
