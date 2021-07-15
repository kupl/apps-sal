N,X,Y=map(int,input().split())
X,Y=X-1,Y-1
d=[0]*N
for i in range(N-1):
  for j in range(i+1,N):
    a=min(abs(j-i),abs(X-i)+1+abs(j-Y))
    d[a]+=1
for i in range(1,N):
  print(d[i])
