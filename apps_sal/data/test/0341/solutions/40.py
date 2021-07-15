n,k=map(int,input().split())
B=list(map(int,input().split()))
S=list(input())
A=[[] for i in range(k)]
for i in range(n):
  if S[i]=="s":
    A[i%k].append(0)
  elif S[i]=="p":
    A[i%k].append(1)
  else:
    A[i%k].append(2)
ans=0
for i in range(k):
  f=0
  for j in range(len(A[i])):
    if f==0:
      ans=ans+B[A[i][j]]
      if j!=len(A[i])-1:
        if A[i][j]==A[i][j+1]:
          f=1
    else:
      f=0
print(ans)
