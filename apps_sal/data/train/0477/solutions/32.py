class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(n):
            s = ''
            for char in n:
                if char == '0':
                    s += '1'
                else:
                    s += '0'
            return s

        def generater(n):
            dp = [-1] * n
            dp[0] = '0'
            for i in range(1, len(dp)):
                dp[i] = dp[i - 1] + '1' + invert(dp[i - 1])[::-1]
            return dp[-1]
        return generater(n)[k - 1]
