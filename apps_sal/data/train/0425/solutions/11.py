class Solution:

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = (dividend < 0) is (divisor < 0)
        (dividend, divisor) = (abs(dividend), abs(divisor))
        result = 0
        while dividend >= divisor:
            (newDivisor, rate) = (divisor, 1)
            while dividend >= newDivisor:
                dividend -= newDivisor
                result += rate
                newDivisor <<= 1
                rate <<= 1
        if not flag:
            result = 0 - result
        return min(max(-2147483648, result), 2147483647)
