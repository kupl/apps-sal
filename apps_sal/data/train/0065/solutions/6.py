import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    A.append(0)
    A.append(0)

    DP0=[1<<30]*(n+3)
    DP1=[1<<30]*(n+3)

    DP0[0]=0

    for i in range(n):
        if A[i]==0 and A[i+1]==0:
            DP1[i+1]=min(DP1[i+1],DP0[i])
            DP1[i+2]=min(DP1[i+2],DP0[i])

        elif A[i]==0 and A[i+1]==1:
            DP1[i+1]=min(DP1[i+1],DP0[i])
            DP1[i+2]=min(DP1[i+2],DP0[i]+1)

        elif A[i]==1 and A[i+1]==0:
            DP1[i+1]=min(DP1[i+1],DP0[i]+1)
            DP1[i+2]=min(DP1[i+2],DP0[i]+1)

        elif A[i]==1 and A[i+1]==1:
            DP1[i+1]=min(DP1[i+1],DP0[i]+1)
            DP1[i+2]=min(DP1[i+2],DP0[i]+2)

        DP0[i+1]=min(DP0[i+1],DP1[i])
        DP0[i+2]=min(DP0[i+2],DP1[i])

    print(min(DP0[n],DP1[n]))

    

    

    
    
    

