class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9 + 7
        # dp[i][j] records the value of sequence of i elements with j being the last element
        dp = [[0]*7 for _ in range(n+1)]
        # initialize
        dp[0][0] = 1
        for i in range(1,7):
            dp[1][i] = 1
        for i in range(2,n+1):
            for j in range(1,7):
                for z in range(7):
                    if j==z:
                        continue
                    for k in range(1,min(rollMax[j-1],i)+1):
                        dp[i][j] += dp[i-k][z]
                        dp[i][j] %= mod
        return sum([dp[n][i] for i in range(1,7)])%mod
            

