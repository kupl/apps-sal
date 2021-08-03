class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(bin):
            bin = list(bin)
            for i in range(len(bin)):
                if bin[i] == '1':
                    bin[i] = '0'
                else:
                    bin[i] = '1'
            return ''.join(bin)
        bin_n = bin(n)[2:]
        dp = ['0'] * n
        for i in range(1, n):
            dp[i] = dp[i - 1] + '1' + invert(dp[i - 1])[::-1]
        return dp[-1][k - 1]
