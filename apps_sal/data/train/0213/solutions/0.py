class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if abs(n) == 1:
            if n == 1:
                return x
            else:
                return 1 / x
        if n > 0:
            a, b = int(n // 2), n % 2
        else:
            a, b = -int(-n // 2), -(n % 2)
        y = self.myPow(x, a)
        z = self.myPow(x, b)
        return y * y * z
