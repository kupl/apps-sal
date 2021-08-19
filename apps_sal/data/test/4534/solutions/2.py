class Solution:

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, rowIndex + 1):
            res += [1]
            for j in range(len(res) - 2, -1, -1):
                if j > 0:
                    res[j] = res[j] + res[j - 1]
                else:
                    res[j] = 1
        return res
