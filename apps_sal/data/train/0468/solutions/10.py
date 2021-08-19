class Solution:

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        st = ''
        if numerator == 0:
            return '0'
        if numerator * denominator < 0:
            st = '-'
        numerator = int(abs(numerator))
        denominator = int(abs(denominator))
        if numerator >= denominator:
            st += str(numerator // denominator)
            numerator %= denominator
        else:
            st += '0'
        position = {}
        fraction = ''
        repeatedPos = -1
        while numerator > 0:
            if numerator in position:
                repeatedPos = position[numerator]
                break
            num = numerator * 10
            val = num // denominator
            position[numerator] = len(fraction)
            fraction += str(val)
            numerator = num % denominator
        if len(fraction) > 0:
            st += '.' + (fraction if repeatedPos == -1 else fraction[:repeatedPos] + '(' + fraction[repeatedPos:] + ')')
        return st
