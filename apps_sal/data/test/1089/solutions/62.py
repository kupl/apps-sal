n,m,k=map(int,input().split())
M=10**9+7
c=1
a=0
for i in range(1,k-1):c=(c*(n*m-1-i)*pow(i,M-2,M))%M
for i in range(n):a=(a+i*(n-i)*(m**2)*c)%M
for i in range(m):a=(a+i*(m-i)*(n**2)*c)%M
print(a)
