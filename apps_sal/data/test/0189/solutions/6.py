n=int(input())
l=list(map(int,input().split()))
mincost=100000
ans=0
for t in range(1,101):
    curcost=0
    for i in l:
        if i==t:
            continue
        else:
            curcost+=abs(t-i)-1
    if curcost<mincost:
        mincost=curcost
        ans=t
print(ans,mincost)
