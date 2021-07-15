import sys
input = sys.stdin.readline

q=int(input())

for testcases in range(q):
    n=int(input())
    f=[tuple(map(int,input().split())) for i in range(n)]

    
    DP0=[0]*n
    DP1=[0]*n
    DP2=[0]*n

    DP1[0]=f[0][1]
    DP2[0]=f[0][1]*2

    for i in range(1,n):
        x=f[i-1][0]
        y=f[i][0]

        if y==x:
            DP0[i]=min(DP1[i-1],DP2[i-1])
            DP1[i]=f[i][1]+min(DP0[i-1],DP2[i-1])
            DP2[i]=f[i][1]*2+min(DP0[i-1],DP1[i-1])

        elif y==x+1:
            DP0[i]=min(DP0[i-1],DP2[i-1])
            DP1[i]=f[i][1]+min(DP0[i-1],DP1[i-1])
            DP2[i]=f[i][1]*2+min(DP0[i-1],DP1[i-1],DP2[i-1])

        elif y==x+2:
            DP0[i]=min(DP0[i-1],DP1[i-1])
            DP1[i]=f[i][1]+min(DP0[i-1],DP1[i-1],DP2[i-1])
            DP2[i]=f[i][1]*2+min(DP0[i-1],DP1[i-1],DP2[i-1])

        elif y==x-1:
            DP0[i]=min(DP0[i-1],DP1[i-1],DP2[i-1])
            DP1[i]=f[i][1]+min(DP1[i-1],DP2[i-1])
            DP2[i]=f[i][1]*2+min(DP0[i-1],DP2[i-1])

        elif y==x-2:
            DP0[i]=min(DP0[i-1],DP1[i-1],DP2[i-1])
            DP1[i]=f[i][1]+min(DP0[i-1],DP1[i-1],DP2[i-1])
            DP2[i]=f[i][1]*2+min(DP1[i-1],DP2[i-1])
            
        else:
            DP0[i]=min(DP0[i-1],DP1[i-1],DP2[i-1])
            DP1[i]=f[i][1]+min(DP0[i-1],DP1[i-1],DP2[i-1])
            DP2[i]=f[i][1]*2+min(DP0[i-1],DP1[i-1],DP2[i-1])

    print(min(DP0[n-1],DP1[n-1],DP2[n-1]))
            
            
            

    

