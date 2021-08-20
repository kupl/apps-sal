class Solution:

    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        (one, m) = (0, 1)
        while m <= n:
            one += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return one
