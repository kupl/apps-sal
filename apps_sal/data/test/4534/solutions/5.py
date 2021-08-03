class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for n in range(rowIndex + 1):
            num = 1
            for i in range(n):
                num = int(num * (rowIndex - i) / (i + 1))
            result = result + [num]
        return result
