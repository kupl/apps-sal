N,A,B=map(int,input().split())
s=(N%(A+B)>A)
t=not s
print(A*(N//(A+B))+s*A+t*N%(A+B))
