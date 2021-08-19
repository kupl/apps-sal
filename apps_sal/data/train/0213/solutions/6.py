class Solution:

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return self.myPow(x * x, (n - 1) / 2) * x
