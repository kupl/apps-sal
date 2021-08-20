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
        res = 1
        while n > 0:
            cnt = 1
            mul = x
            while cnt + cnt <= n:
                mul = mul * mul
                cnt += cnt
            n = n - cnt
            res = mul * res
        if n % 2 == 1:
            res = res * x
        return res
