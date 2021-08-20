class Solution:

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        for i in range(n + 1):
            res.append(-1)
        for i in range(n + 1):
            for j in range(i):
                res[j] = max(j, res[j])
                res[i] = max(res[i], res[j] * (i - j))
        return res[n]
