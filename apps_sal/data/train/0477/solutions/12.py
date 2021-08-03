class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        dp = [None] * (n)
        dp[0] = '0'
        for i in range(1, n):
            m = ''
            inv = self.invert(dp[i - 1], m)
            rev = self.reverse(inv)
            dp[i] = dp[i - 1] + '1' + rev
        return dp[-1][k - 1]

    def reverse(self, string):
        return string[::-1]

    def invert(self, string, m):
        for i in range(len(string)):
            if string[i] == '1':
                m += '0'
            else:
                m += '1'
        return m
