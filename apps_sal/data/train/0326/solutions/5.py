class Solution:

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        count = len(s)
        if count <= 1:
            return s
        result = []
        deltSmall = numRows - 1
        deltBig = 2 * deltSmall
        for i in range(0, numRows):
            k = i
            if i == 0 or i == deltSmall:
                while k < count:
                    result.append(s[k])
                    k += deltBig
            else:
                while k < count:
                    top = k - k % deltSmall
                    bottom = top + deltSmall
                    result.append(s[k])
                    nextk = 2 * bottom - k
                    if nextk < count:
                        result.append(s[nextk])
                    k += deltBig
        return ''.join(result)
