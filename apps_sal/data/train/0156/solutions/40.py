class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        dp =[[-1 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        
        for i in range(len(s)+1):
            for j in range(len(t)+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # for i in dp:
        #     print(i)
        lcs =''
        i,j=len(s),len(t)
        while i>0 and j>0:
            if s[i-1]==t[j-1]:
                lcs += s[i-1]
                i-=1
                j-=1
            else:
                if dp[i][j-1]>dp[i-1][j]:
                    j-=1
                    lcs += t[j]
                else:
                    i-=1
                    lcs+=s[i]
        while i>0:
            i-=1
            lcs+=s[i]
        while j>0:
            j-=1
            lcs +=t[j]
        return lcs[::-1]
