a,b,c=map(int, input().split())
p=998244353

A=(a*(a+1)//2)%p
B=(b*(b+1)//2)%p
C=(c*(c+1)//2)%p
print(A*B*C%p)
