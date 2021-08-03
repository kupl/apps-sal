class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        counts, length, digits = 0, len(str(n)), [int(i) for i in str(n)]
        counts = digits[0] * (length - 1) * (10 ** (length - 2)) + min(digits[0] - 1, 1) * (10 ** (length - 1)) + \
            max(2 - digits[0], 0) * (n - 10 ** (length - 1) + 1) + Solution().countDigitOne(n - digits[0] *
                                                                                            (10 ** (length - 1)))
        return int(counts)
