class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0] * (59)
        memo[1] = 1
        for i in range(2, n + 1):
            tmp = []
            for j in range(1, i):
                memo[i] = max((memo[i], max(memo[j], j) * max(i - j, memo[i - j])))
        return memo[n]
