class Solution:

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[]] * numRows
        for i in range(numRows):
            if i == 0:
                result[0] = [1]
            if i == 1:
                result[1] = [1, 1]
            if i > 1:
                temp = []
                for k in range(i + 1):
                    left = result[i - 1][k - 1] if k >= 1 else 0
                    right = result[i - 1][k] if k < i else 0
                    temp.append(left + right)
                result[i] = temp
        return result
