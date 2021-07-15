class Solution:
    def knightDialer(self, n: int) -> int:
        if n==1:
            return 10
        numpad = {'0':['4','6'],'1':['6','8'],'2':['7','9'],'3':['4','8'],'4':['0','3','9'],'6':['0','1','7'],'7':['2','6'],'8':['1','3'],'9':['4','2']}
        dp={}
        for i in ['0','1','2','3','4','6','7','8','9']:
            dp[i]=[]
            dp[i].append(1)
        for i in range(1,n):
            for j in ['0','1','2','3','4','6','7','8','9']:
                dp[j].append(0)
                for k in numpad[j]:
                    dp[j][i]+=dp[k][i-1]
                dp[j][i]%=(1000000007)
        res=0
        for i in ['0','1','2','3','4','6','7','8','9']:
            res+=dp[i][n-1]
            res%=(1000000007)
        return res
