class Solution:
    def numSquarefulPerms(self, A):
        A.sort()
        N = len(A)
        graph = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if i==j: continue
                if int((A[i]+A[j])**0.5)**2==(A[i]+A[j]):
                    graph[i][j]=1
                    graph[j][i]=1


        dp=[[0]*N for i in range(1<<N)]
        for i in range(N):
            dp[1<<i][i]=1
        for s in range(1<<N):
            for i in range(N):
                if not dp[s][i]: continue
                for j in range(N):
                    if not graph[i][j]: continue
                    if s&(1<<j): continue
                    if j>0 and s&(1<<(j-1)) and A[j]==A[j-1]:continue
                    dp[s|(1<<j)][j]+=dp[s][i]

        ans=0
        for i in range(N):
            ans+=dp[-1][i]

        return ans
        

        

