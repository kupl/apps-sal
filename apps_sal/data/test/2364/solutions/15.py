MOD=998244353
def f(n):
    if(n==0):
        return 1
    if(n==1):
        return 3
    return ((n+2)*pow(2,n-1,MOD))%MOD
n=int(input())
ar=list(map(int,input().split()))[::-1]
S=0
for i in range(n):
    S+=ar[i]*f(i)
print(S%MOD)

