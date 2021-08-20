class Solution:

    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        dp = [1, 2]
        for i in range(2, 32):
            dp.append(dp[i - 1] + dp[i - 2])
        bnum = bin(num)[2:]
        size = len(bnum)
        ans = dp[size]
        for i in range(1, size):
            if bnum[i - 1] == bnum[i] == '1':
                break
            if bnum[i - 1] == bnum[i] == '0':
                ans -= dp[size - i] - dp[size - i - 1]
        return ans
