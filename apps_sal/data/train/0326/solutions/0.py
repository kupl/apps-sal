class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ['' for i in range(numRows)]
        row = 0
        step = 1
        for c in s:
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            zigzag[row] += c
            row += step
        return ''.join(zigzag)
