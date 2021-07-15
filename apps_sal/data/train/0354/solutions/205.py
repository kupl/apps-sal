class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0 for _ in range(16)] for _ in range(7)] for _ in range(n+1)]
        mod = 10**9+7

        for i in range(1, n+1):
            for j in range(1, 7):# 投掷的数
                if(i == 1):# 第一次投掷
                    dp[i][j][1] = 1
                    continue

                # 数字 j 连续出现 k 次
                for k in range(2, rollMax[j-1]+1):
                    dp[i][j][k] = dp[i-1][j][k-1]
                
                # 前一次投出的数不是 j
                temp = 0
                for l in range(1, 7):
                    if(l == j):
                        continue
                    for k in range(1, 16):
                        temp += dp[i-1][l][k]
                        temp %= mod
                dp[i][j][1] = temp
        
        res = 0
        for j in range(1, 7):
            for k in range(1, 16):
                res += dp[n][j][k]
                res %= mod
        return res
