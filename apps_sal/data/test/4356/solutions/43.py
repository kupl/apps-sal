N,M=map(int,input().split())
A=[[] for i in range(N)]
B=[[] for i in range(M)]
for i in range(N):
  L=list(input())
  A[i]=L
for i in range(M):
  L=list(input())
  B[i]=L
for i in range(N-M+1):
  for j in range(N-M+1):
    ans=0
    for k in range(M):
      for s in range(M):
        #i,jを始点とした
        if B[k][s]!=A[i+k][j+s]:
          ans=-1
        if k==M-1 and s==M-1:
          if ans==0:
            print("Yes")
            return
print("No")
