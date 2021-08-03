class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        p = 2
        while n > 1:
            while n % p == 0:
                res += p
                n /= p
            p += 1
        return res
