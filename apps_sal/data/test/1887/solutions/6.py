import sys
input = sys.stdin.readline

n=int(input())
H0=list(map(int,input().split()))
H1=list(map(int,input().split()))

DP0=[0]*(n+5)
DP1=[0]*(n+5)

DP0[0]=H0[0]
DP1[0]=H1[0]

for i in range(1,n):
    DP0[i]=max(DP1[i-1],DP1[i-2],DP0[i-2])+H0[i]
    DP1[i]=max(DP0[i-1],DP0[i-2],DP1[i-2])+H1[i]

print(max(max(DP0),max(DP1)))


