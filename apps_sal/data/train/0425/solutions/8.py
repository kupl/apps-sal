class Solution:

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend < 0 and divisor > 0 or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        summ = 0
        count = 0
        res = 0
        a = abs(dividend)
        b = abs(divisor)
        while a >= b:
            summ = b
            count = 1
            while summ + summ <= a:
                summ += summ
                count += count
            a -= summ
            res += count
        if dividend < 0 and divisor > 0 or (dividend > 0 and divisor < 0):
            res = 0 - res
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        return res
