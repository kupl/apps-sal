class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        tag = 1 if (dividend < 0) is (divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor == 0:
            return float('inf')
        count = 0

        while dividend >= divisor:
            mul = 1
            t = divisor
            while dividend > (t << 1):
                t <<= 1
                mul <<= 1
            dividend -= t
            count += mul
            #print(dividend, mul)
        return min(max(-2147483648, count * tag), 2147483647)
