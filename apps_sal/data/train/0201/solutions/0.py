class Solution:
    hash = {}

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1 or n == 2:
            return n
        try:
            return self.hash[n]
        except KeyError:
            pass
        resSum = 0
        for i in range(n):
            tempSum = self.numTrees(i) * self.numTrees(n - (i + 1))
            resSum += tempSum
        self.hash[n] = resSum
        return resSum
