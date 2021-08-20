class Solution:

    def nextGreaterElement(self, n):
        """
        44332211 -> -1
        33442211 -> 34112234
        22443311 -> 23112344
        :type n: int
        :rtype: int
        """
        s = str(n)
        l = len(s)
        digits = [int(c) for c in s]
        i = l - 1
        while i > 0 and s[i] <= s[i - 1]:
            i -= 1
        if i == 0:
            return -1
        j = l - 1
        while j > i - 1 and s[j] <= s[i - 1]:
            j -= 1
        (digits[i - 1], digits[j]) = (digits[j], digits[i - 1])
        res = digits[:i] + sorted(digits[i:])
        res = int(''.join((str(d) for d in res)))
        if res > 2 ** 31:
            return -1
        return res
