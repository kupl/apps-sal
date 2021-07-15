n,a,b=map(int,input().split())
m=10**9+7
ALL=pow(2,n,m)-1
x=y=1

for i in range(b):
    x=x*(i+1)%m
    y=y*(n-i)%m
    if i+1==a:
        a=b
        ALL-=y*pow(x,m-2,m)

print(ALL%m)
