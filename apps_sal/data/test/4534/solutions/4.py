class Solution:

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = [1]
        for i in range(rowIndex):
            l = [j + k for (j, k) in zip([0] + l, l + [0])]
        return l
