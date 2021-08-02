class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a = [1]
        i = 0
        b = [1]
        while i < rowIndex:
            a.append(0)
            b = a[:]
            for j in range(i + 2):
                b[j] = a[j] + a[i - j + 1]
            a = b
            i += 1
        return b
