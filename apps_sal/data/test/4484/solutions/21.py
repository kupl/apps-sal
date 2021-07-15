from math import factorial
N,M=map(int,input().split())
ans=0
if abs(N-M)>1:
    ans=0
else:
    if N==M:
        a=N
        b=M
        ans=factorial(a)*factorial(b)*2
    else:
        a=max(N,M)
        b=min(N,M)
        ans=factorial(a)*factorial(b)
print(ans%(10**9+7))
