class Solution:

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if abs(dividend) < abs(divisor):
            return 0
        (sum, count, result) = (0, 0, 0)
        (a, b) = (abs(dividend), abs(divisor))
        while a >= b:
            sum = b
            count = 1
            while sum + sum < a:
                sum += sum
                count += count
            a -= sum
            result += count
        if dividend < 0 and divisor > 0 or (dividend > 0 and divisor < 0):
            result = 0 - result
        return min(result, 2147483647)
