class Solution:    
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[n if i > 0 else 0] * (k + 1) for i in range(n + 1)]
        
        def cost(v):
            return (1 + len(str(v))) if v > 1 else v
        
        for i in range(n):
            for j in range(k + 1):
                if j:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
                take = 0
                for x in range(i + 1)[::-1]:
                    if s[x] != s[i]:
                        take += 1
                    if take > j:
                        break
                    dp[i + 1][j - take] = min(dp[i + 1][j - take], dp[x][j] + cost(i - x - take + 1))        
        return min(dp[n])
