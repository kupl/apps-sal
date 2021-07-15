class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        def lcs(a,b):
            n, m = len(a),len(b)
            dp = [['' for j in range(m+1)] for i in range(n+1)]
            for i in range(n):
                for j in range(m):
                    if a[i]==b[j]:
                        dp[i+1][j+1]=dp[i][j]+a[i]
                    else:
                        dp[i+1][j+1]=max(dp[i+1][j], dp[i][j+1] , key =len)
            return dp[-1][-1]
        res , i ,j = '',0,0
        for c in lcs(a,b):
            while a[i]!=c:
                res+=a[i]
                i+=1
            while b[j]!=c:
                res+=b[j]
                j+=1
            res+=c
            i+=1
            j+=1
        res+= a[i:]+b[j:]
        return res
