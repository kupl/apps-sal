class Solution:

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for i in range(n)]
        (start, end) = (0, n - 1)
        count = 1
        for j in range(int(n / 2)):
            for i in range(start, end + 1):
                matrix[start][i] = count
                count += 1
            for i in range(start + 1, end + 1):
                matrix[i][end] = count
                count += 1
            for i in range(end - 1, start - 1, -1):
                matrix[end][i] = count
                count += 1
            for i in range(end - 1, start, -1):
                matrix[i][start] = count
                count += 1
            start += 1
            end -= 1
        if n % 2 != 0:
            matrix[start][end] = count
        return matrix
