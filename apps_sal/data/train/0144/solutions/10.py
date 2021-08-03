class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = 2
        s = 0
        while f * f <= n:
            while n % f == 0:
                s += f
                n = int(n / f)
            f += 1
        if n > 1:
            s += n
        return int(s)
