import math
n,m=map(int,input().split())
N=math.factorial(n)
if abs(n-m)>1:
    print(0)
elif abs(n-m)==0:
    print(2*N*N%(10**9+7))
elif n>m:
    print((N*N//n)%(10**9+7))
else:
    print(N*N*m%(10**9+7))
