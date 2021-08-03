class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0] * (n + 1)
        memo[0] = 0
        memo[1] = 1

        for i in range(2, n + 1):
            maxprod = 1
            for j in range(1, i):
                maxprod = max(maxprod, max(j, memo[j]) * max((i - j), memo[i - j]))
            memo[i] = maxprod

        return memo[n]
