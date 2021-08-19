class Solution:

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        if n == 4:
            return 4
        if n > 4:
            if n % 3 == 0:
                return 3 ** int(n / 3)
            if n % 3 != 0 and (n - 2) % 3 == 0:
                return 3 ** int((n - 2) / 3) * 2
            else:
                return 3 ** int((n - 2) / 3) * 4
