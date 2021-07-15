def main():
    N=int(input())
    A=list(map(int,input().split()))
    AA=[(v,i) for i,v in enumerate(A)]
    AA.sort(reverse=True)
    dp=[[0]*(N+1) for _ in range(N+1)]
    for len in range(1,N+1):
        val,index=AA[len-1]
        for x in range(0,len+1):
            y=len-x
            if x==0:
                dp[x][y]=dp[x][y-1]+val*abs(N-y-index)
            elif y==0:
                dp[x][y]=dp[x-1][y]+val*abs(index-x+1)
            else:
                dp[x][y]=max(dp[x][y-1]+val*abs(N-y-index),dp[x-1][y]+val*abs(index-x+1))
    maxes=[]
    for i in dp:
        maxes.append(max(i))
    return max(maxes)
print(main())
