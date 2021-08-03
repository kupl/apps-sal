class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        is_neg = (numerator > 0) ^ (denominator > 0)
        numerator = abs(numerator)
        denominator = abs(denominator)
        nd = dict()
        ret = [str(numerator // denominator) + "."]
        while numerator:
            numerator = 10 * (numerator % denominator)
            n_s = str(numerator // denominator)
            if numerator in nd:
                ret.insert(nd[numerator], '(')
                ret.append(')')
                break
            else:
                ret.append(n_s)
            nd[numerator] = len(ret) - 1

        ret = "".join(ret)
        while ret[-1] == "0":
            ret = ret[:-1]
        if ret[-1] == ".":
            ret = ret[:-1]
        if is_neg:
            ret = "-" + ret

        return ret
