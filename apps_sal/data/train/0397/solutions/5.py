class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        i = 0
        while pow(10, i) <= n:
            i += 1
        if i == 1:
            return 1

        s = n % pow(10, i - 1)
        temp = self.countDigitOne(s)

        t = n // pow(10, i - 1)
        if t > 1:
            temp1 = pow(10, i - 1)
        elif t == 1:
            temp1 = s + 1
        temp2 = t * (i - 1) * pow(10, i - 2)
        return temp + temp1 + temp2
