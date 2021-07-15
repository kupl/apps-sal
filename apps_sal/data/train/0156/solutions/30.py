class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        n=len(a)
        m=len(b)
        dp=[['-1']*(n+1) for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if(i==0 or j==0):
                    dp[i][j]=''
                else:
                    if(a[j-1]==b[i-1]):
                        dp[i][j]=a[j-1]+dp[i-1][j-1]
                    else:
                        s1=dp[i-1][j]
                        s2=dp[i][j-1]
                        if(len(s1)>len(s2)):
                            dp[i][j]=s1
                        else:
                            dp[i][j]=s2
        s=dp[-1][-1][::-1]
        result=''
        I=0
        J=0
        for i in s:
            while(a[I]!=i):
                result=result+a[I]
                I=I+1
            while(b[J]!=i):
                result=result+b[J]
                J=J+1
            result=result+i
            I=I+1
            J=J+1

        return(result+a[I:]+b[J:])
