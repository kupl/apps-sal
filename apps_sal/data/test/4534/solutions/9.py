class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0: return []
        result = [0 for _ in range(rowIndex + 1)]
        result[0] = 1
        for i in range(1, rowIndex + 1):
            result[i] = 1
            for j in range(i - 1, 0, -1):
                result[j] = result[j] + result[j - 1]
        return result
