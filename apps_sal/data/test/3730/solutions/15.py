n = int(input())
a = [int(i) for i in input().split()]
l,r = [1]*n,[1]*n

for i in range(1,n):
    if a[i-1]<a[i]: l[i]+=l[i-1]

for i in range(n-2,0,-1):
    if a[i+1]>a[i]: r[i]+=r[i+1]

ans = max(l)
if ans<n: ans+=1
for i in range(1,n-1):
    if a[i-1]+1<a[i+1]: ans=max(ans,l[i-1]+r[i+1]+1)
print(ans)
