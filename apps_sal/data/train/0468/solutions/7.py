class Solution:

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '' if numerator * denominator >= 0 else '-'
        (numerator, denominator) = (abs(numerator), abs(denominator))
        (integer, ret) = (str(numerator // denominator), '')
        (remainers, rem) = ({}, numerator % denominator)
        if rem:
            integer += '.'
        while rem and rem not in remainers:
            remainers[rem] = len(ret)
            rem *= 10
            ret += str(rem // denominator)
            rem %= denominator
        if rem:
            ret = ret[:remainers[rem]] + '(' + ret[remainers[rem]:] + ')'
        return sign + integer + ret
