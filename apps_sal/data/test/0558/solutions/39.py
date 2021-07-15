M=998244353
n,m,k=map(int,input().split())
p,c=[m]*n,[1]*n
for i in range(1,n):
  p[i]=p[i-1]*(m-1)%M
  c[i]=c[i-1]*(n-i)*pow(i,M-2,M)%M
print(sum(p[n-i-1]*c[i]%M for i in range(k+1))%M)
