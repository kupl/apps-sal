N,M=map(int,input().split())
x=[0]*(N+1)
for i in range(M) :
  a,b=map(int,input().split())
  for j in range(1,N+1) :
    if a==j or b==j :
      x[j]+=1
for i in range(1,N+1) :
  print(x[i])
