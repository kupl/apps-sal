class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int     
        """
        M = [0 for x in range(n)]
        M[0] = 1
        for i in range(1, n):
            for j in range(1, i):
                M[i] += M[j - 1] * M[i - j - 1]
            M[i] += M[i - 1] * 2
        return M[n - 1]
