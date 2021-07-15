n=int(input())
a=tuple(map(int,input().split(' ')))
r,ans,tsum,txor=0,0,0,0
for l in range(n):
    while r<n and txor^a[r]==tsum+a[r]:
        txor = txor^a[r]
        tsum = tsum+a[r]
        r += 1
    ans += r-l
    if l==r:
        r+=1
    else:
        txor = txor^a[l]
        tsum -= a[l]
print(ans)
