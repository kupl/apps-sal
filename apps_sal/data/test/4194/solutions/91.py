n,m= map(int, input().split())
a=list(map(int, input().split()))
s=0
for i in range(m):
    s=s+a[i]
if s<=n:print(n-s)
else:print(-1)
