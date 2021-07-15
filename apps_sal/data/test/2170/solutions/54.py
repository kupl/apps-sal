n,m=map(int,input().split())
M,F=10**9+7,[1]
for i in range(m): F+=[-~i*F[i]%M]
print(sum((-1)**k*F[m-k]*pow(F[k]*F[n-k]*F[m-n]**2,-1,M) for k in range(n+1))*F[n]*F[m]%M)
