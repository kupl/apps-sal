n,m = map(int,input().split())
a = list(sorted(map(int, input().split())))
ans  = 100500
for i in range(m-n+1):
    ans = min(ans, a[i+n-1]-a[i])
print(ans)
