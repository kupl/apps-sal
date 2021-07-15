N,X=map(int,input().split())
L=list(map(int,input().split()))
ans=0

for i in range(1,N+1):
  if ans>=X:
    if ans==X:
      print(i)
      break
    else:
      print(i-1)
      break
  ans+=L[i-1]
else:
  print(N+1)
