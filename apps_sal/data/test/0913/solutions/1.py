from math import ceil
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=0
m=0
for i in range(n):
    d=a[i]-b[i]
    if d>0:
        p+=d
    else:
        m-=d
if p==0:
    print(-1)
else:
    print(m//p+1)

