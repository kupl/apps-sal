n,m = map(int,input().split())
a = list(map(int,input().split()))
for i in range(m):
    n -= a[i]
print(max(n,-1))
