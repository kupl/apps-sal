n=int(input())
a=[int(s) for s in input().split()]
a.sort()
cur=1
ans=0
for i in range(n):
    if a[i]>=cur:
        cur+=1
        ans+=1
print(ans)
