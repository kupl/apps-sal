class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        '''
        d*f = total possible roll outcomes


        d=2 f=6 target=7

        1+6 2+5 3+4 4+3 5+2 6+1

            0 1 2 3 4 5 6 7
            0 1 1 1 1 1 1 0
            0 0 1 2 3 4 5 6
        dp[d][i] += dp[d-1][i-j] when j = 1...6 and i >= j

        '''

        dp = [[0 for _ in range(target + 1)] for _ in range(d)]

        # initialize the first row with up to f
        for i in range(1, min(f + 1, target + 1)):
            dp[0][i] = 1

        for i in range(1, d):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]
                        dp[i][j] %= (10**9) + 7

        # print(dp)
        return dp[d - 1][target]
