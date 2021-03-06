class Solution:

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        while n > 4:
            n = n - 3
            res *= 3
        return res * n
