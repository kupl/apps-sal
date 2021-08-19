class Solution:

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        for d in range(2, n + 1):
            while n % d == 0:
                s += d
                n /= d
        return s
