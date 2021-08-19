class Solution:

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1
        elif n > 1000:
            return self.myPow(self.myPow(x, 1000), n // 1000) * self.myPow(x, n % 1000)
        else:
            return x * self.myPow(x, n - 1)
