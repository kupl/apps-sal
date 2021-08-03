class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            if len(result) < i:
                result.append([])
            result[i - 1].append(1)
            count = 0
            while len(result[i - 1]) < i - 1:
                result[i - 1].append(result[i - 2][count] + result[i - 2][count + 1])
                count += 1
            result[i - 1].append(1)
        return result
