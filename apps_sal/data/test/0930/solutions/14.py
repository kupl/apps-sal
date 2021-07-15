M=10**9+7;n,k=map(int,input().split());a=c=p=1
for i in range(1,min(n,k+1)):c=c*(n-i+1)*(n-i)%M;p=p*i*i%M;a+=c*pow(p,M-2,M)
print(a%M)
