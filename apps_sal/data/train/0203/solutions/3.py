class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = m - 1
        b = n - 1
        ret = 1
        for i in range(b):
            ret = ret * (a + b - i) / (b - i)
        return round(ret)
