class Solution:

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        list_string = [''] * numRows
        (index, step) = (0, 1)
        for i in s:
            list_string[index] += i
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(list_string)
