import bisect
n=int(input())
a=list(map(int,input().split()))
a.sort()
#print(a)
ans=0
for i in range(n-1,1,-1):
    for j in range(i-1,0,-1):
        t=bisect.bisect_right(a,a[i]-a[j])
        #print(a[i],a[j],a[i]-a[j],t,j-t)
        if j-t>0:
            ans+=j-t
print(ans)

