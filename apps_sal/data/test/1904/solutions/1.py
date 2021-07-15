import sys
input = sys.stdin.readline

n=int(input())
S=input()
A=list(map(int,input().split()))

DP=[0]*4#None,"h","ha","har"まででくいとめる
DP[0]=0

for i in range(n):
    if S[i]=="h":
        DP[0]+=A[i]
    elif S[i]=="a":
        DP[1]=min(DP[0],A[i]+DP[1])
    elif S[i]=="r":
        DP[2]=min(DP[1],A[i]+DP[2])
    elif S[i]=="d":
        DP[3]=min(DP[2],A[i]+DP[3])
        
print(min(DP))

