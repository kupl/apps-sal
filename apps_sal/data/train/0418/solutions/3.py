class Solution:

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.integerReplacementDP(n)
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n / 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

    def integerReplacementDP(self, n, dp=None):
        if dp is None:
            dp = {}
        if n == 1:
            return 0
        if n not in dp:
            if n % 2 == 0:
                dp[n] = 1 + self.integerReplacementDP(n / 2, dp=dp)
            else:
                dp[n] = 1 + min(self.integerReplacementDP(n + 1, dp=dp), self.integerReplacementDP(n - 1, dp=dp))
        return dp[n]

    def integerReplacementBitwise(self, n):
        """

        5 -> 4 -> 2 -> 1
        5 -> 6 -> 3 -> 2 -> 1

        101 100
        101 110   

        11 10
        """
        count = 0
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            elif n == 3 or bin(n + 1).count('1') > bin(n - 1).count('1'):
                n -= 1
            else:
                n += 1
            count += 1
        return count
