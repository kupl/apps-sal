class Solution:

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        A = []
        for i in range(numRows):
            A.append([1 for _ in range(i + 1)])
            for j in range(1, i):
                A[i][j] = A[i - 1][j - 1] + A[i - 1][j]
        return A
