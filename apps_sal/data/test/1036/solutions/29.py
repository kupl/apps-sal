n,k=map(int, input().split());S=input();d=[list(S) for _ in range(k+1)]
for i in range(k):
  for j in range(n):a=d[i][j];b=d[i][(j+pow(2,i))%n];d[i+1][j]=a if b+a in'SRPS'else b
print(d[k][0])
