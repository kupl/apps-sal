class Solution(object):

    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = bin(num)[2:][::-1]
        dp = [[1, 1] for _ in range(len(A))]
        res = 1 if A[0] == '0' else 2
        for i in range(1, len(A)):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] = dp[i - 1][0]
            if A[i - 1:i + 1] == '01':
                res += dp[i][0]
            elif A[i - 1:i + 1] == '11':
                res = dp[i][0] + dp[i][1]
        return res
