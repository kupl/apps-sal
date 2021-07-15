import sys
input = sys.stdin.readline

T=int(input())
for testcases in range(T):
    n,a,b=list(map(int,input().split()))
    S=list(map(int,list(input().strip())))
    S.append(0)

    ANS=(n+1)*b+n*a

    DP=[[1<<50,1<<50] for i in range(n+1)]
    DP[0][0]=0

    for i in range(1,n+1):
        if S[i-1]==S[i]==0:
            DP[i][0]=min(DP[i-1][0],DP[i-1][1]+a)
            DP[i][1]=min(DP[i-1][0]+a+b,DP[i-1][1]+b)

        else:
            DP[i][1]=min(DP[i-1][0]+a+b,DP[i-1][1]+b)

    #print(DP)

    print(ANS+DP[-1][0])
            

