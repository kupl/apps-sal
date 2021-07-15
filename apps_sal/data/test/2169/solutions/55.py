import sys
input=sys.stdin.readline
H,W,D=map(int,input().split())
cost=[[0 for _ in range((H*W)//D+1)] for i in range(D)]
L=[0]*(H*W)
for i in range(H):
  L1=list(map(int,input().split()))
  for j in range(W):
    L[L1[j]-1]=[i,j]
    if L1[j]%D!=0:
      cost[L1[j]%D][L1[j]//D]=[i,j,0]
    else:
      cost[L1[j]%D][(L1[j]//D)-1]=[i,j,0]
for i in range(D):
  for j in range(1,len(cost[i])):
    if cost[i][j]!=0:
      cost[i][j][2]=cost[i][j-1][2]+abs(cost[i][j][0]-cost[i][j-1][0])+abs(cost[i][j][1]-cost[i][j-1][1])
Q=int(input())
for i in range(Q):
  A,B=map(int,input().split())
  c=A%D
  a=A//D
  b=B//D
  if c==0:
    a,b=a-1,b-1
  print(cost[c][b][2]-cost[c][a][2])
