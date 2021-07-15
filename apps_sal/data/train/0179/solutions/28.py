class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # dp[i][k]: the min length for s[:i+1] with at most k deletion
        # each s[i]: keep or discard
        # if delete: dp[i][j] = dp[i-1][j-1]
        # if keep: delete at most j chars in s[:i+1] that are different from s[i]
        n = len(s)
        dp =[[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(k+1):
                cnt = 0
                d = 0
                for l in range(i, 0, -1):
                    if s[l-1] == s[i-1]:
                        cnt += 1
                    else:
                        d += 1
                    if j - d >= 0:
                        diff = 0
                        if cnt >= 100:
                            diff = 3
                        elif cnt >=10:
                            diff = 2
                        elif cnt >= 2:
                            diff = 1
                            
                        dp[i][j] = min(dp[i][j], dp[l-1][j-d] +1 +diff)
                if j > 0:
                    # delete s[i]
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
        return dp[n][k]
