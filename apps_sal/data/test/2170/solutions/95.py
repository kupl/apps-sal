n,m=map(int,input().split())
M,d=10**9+7,[1]*(n+1)
for i in range(n):
  d[i+1]=((m-i)*((m-n+i)*d[i]+i*d[i-1]*(m-i+1)))%M
print(d[-1])
