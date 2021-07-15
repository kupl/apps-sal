class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # dp[i][j] is to partition s[:i] into j groups
        n = len(s)
        dp = [[float('inf')]*(k+1) for _ in range(n+1)]
        
        dp[0][0] = 0
        def cald(s):
            if len(s)==1:
                return 0
            else:
                lo, hi = 0, len(s)-1
                ans = 0
                while lo<hi:
                    if s[lo]!=s[hi]:
                        ans += 1
                    lo += 1
                    hi -= 1
                return ans

        for i in range(1,n+1): # to s[:i]
            for j in range(1,k+1):
                for h in range(j-1,i): # split into dp[h][] and s[h:i]
                    dp[i][j] = min(dp[i][j], dp[h][j-1]+ cald(s[h:i])  )
        return dp[n][k]
        

