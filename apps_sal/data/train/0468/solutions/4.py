class Solution:
    def fractionToDecimal(self, numerator, denominator):
        res = ""
        if numerator * denominator < 0:
            res = res + "-"
        if numerator % denominator == 0:
            return str(numerator // denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)
        res = res + str(numerator // denominator)
        res = res + "."
        numerator = numerator % denominator
        table = {}
        i = len(res)
        while numerator != 0:
            if numerator not in table:
                table[numerator] = i
            else:
                i = table[numerator]
                res = res[:i] + "(" + res[i:] + ")"
                return res
            numerator = numerator * 10
            res = res + str(numerator // denominator)
            numerator = numerator % denominator
            i = i + 1
        return res
        """
         :type numerator: int
         :type denominator: int
         :rtype: str
         """
