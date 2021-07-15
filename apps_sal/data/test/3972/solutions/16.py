n=int(input())-1;a,b,c,p=1,1,n+1,n
for _ in[0]*n:p+=a-1;a,b,c=b,c,(n*n+p+c)%(10**9+7)
print(c)
