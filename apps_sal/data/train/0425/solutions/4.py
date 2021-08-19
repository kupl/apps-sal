class Solution:

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        (dividend, divisor, div) = (abs(dividend), abs(divisor), abs(divisor))
        res = 0
        q = 1
        while dividend >= divisor:
            dividend -= div
            res += q
            q += q
            div += div
            if dividend < div:
                div = divisor
                q = 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
