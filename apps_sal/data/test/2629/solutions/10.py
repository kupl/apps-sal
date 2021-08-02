class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        nums = list(range(1, n * n + 1))
        matrix = [[nums[-1]]]
        start = n * n - 1

        while start > 0:
            matrix = matrix[::-1]
            matrix = [*zip(*matrix)]
            matrix = [nums[(start - len(matrix[0])):start]] + matrix
            start = start - len(matrix[0])

        return [*map(list, matrix)]
