from math import ceil
n,k=map(int,input().split())
a=list(map(int,input().split()))
l,r=0,10**9
while r-l>1:
    m=(r+l)//2
    count=0
    for i in a:
        count+=ceil(i/m)-1
    if count<=k:
        r=m
    else:
        l=m
print(r)
