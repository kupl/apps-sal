class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp[i][j][k]: after ith throw, the number of sequences which end with j (j in [0,5]) and continous k times (k in [1,15])
        dp = [[[0]*(max(rollMax)+1) for _ in range(6)] for _ in range(n)]
        mod = 10**9 + 7
        for j in range(6):
            dp[0][j][1] = 1
        for i in range(1,n):
            for j in range(6):
                for k in range(1,min(rollMax[j]+1,i+2)):
                    if k == 1:
                        for prevj in range(6):
                            if prevj != j:
                                dp[i][j][k] += sum(dp[i-1][prevj])
                    else:
                        dp[i][j][k] = dp[i-1][j][k-1] 
        return sum([sum(dp[-1][j]) for j in range(6)]) % mod
